def palindromes_between_indices(s):
    letters = [c.lower() for c in s[3:10] if c.isalpha()]
    result = set()

    def generate_palindromes(current, remaining):
        if len(current) >= 5:
            palindrome = current + current[::-1]
            result.add(palindrome)
        if len(current) * 2 < 10:
            for i, char in enumerate(remaining):
                generate_palindromes(current + char, remaining[:i] + remaining[i + 1:])
    generate_palindromes('', letters)
    return result