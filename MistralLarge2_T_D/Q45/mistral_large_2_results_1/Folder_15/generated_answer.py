def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    chars = [c for c in s[1:3] if c.isalpha()]
    chars = ''.join(chars).lower()
    palindromes = set()
    for i in range(len(chars)):
        for j in range(i + 3, len(chars) + 1):
            substring = chars[i:j]
            if is_palindrome(substring):
                palindromes.add(substring)
    return palindromes