def palindromes_between_indices(s):
    letters = [c.lower() for c in s[2:5] if c.isalpha()]
    palindromes = set()

    def generate_palindromes(current, remaining):
        if len(current) >= 3:
            palindrome = current + current[-2::-1]
            palindromes.add(palindrome)
        for i, char in enumerate(remaining):
            generate_palindromes(current + char, remaining[:i] + remaining[i + 1:])
    generate_palindromes('', letters)
    return palindromes