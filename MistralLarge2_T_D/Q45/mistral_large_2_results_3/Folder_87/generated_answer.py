def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    chars = [c for c in s[3:10] if c.isalpha()]
    chars_lower = [c.lower() for c in chars]
    palindromes = set()
    for length in range(3, len(chars_lower) + 1):
        for i in range(len(chars_lower) - length + 1):
            substring = ''.join(chars_lower[i:i + length])
            if is_palindrome(substring):
                palindromes.add(substring)
    return palindromes