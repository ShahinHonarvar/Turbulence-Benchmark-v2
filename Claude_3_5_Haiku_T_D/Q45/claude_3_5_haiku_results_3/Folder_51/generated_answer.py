def palindromes_between_indices(s):
    letters = [char.lower() for char in s[3:6] if char.isalpha()]
    palindrome_set = set()

    def generate_palindromes(current, remaining):
        if len(current) >= 3 and len(current) == len(remaining) * 2 - 1:
            if current == current[::-1]:
                palindrome_set.add(current)
            return
        for i in range(len(remaining)):
            generate_palindromes(current + remaining[i], remaining[:i] + remaining[i + 1:])
    generate_palindromes('', letters)
    return palindrome_set