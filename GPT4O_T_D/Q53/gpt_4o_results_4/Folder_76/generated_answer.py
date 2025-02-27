def palindrome_of_length_at_least_n(s):

    def is_palindrome(substring):
        return substring == substring[::-1]
    s = ''.join(filter(str.isalpha, s)).lower()
    found_palindromes = set()
    for start in range(len(s)):
        for end in range(start + 137, len(s) + 1):
            substring = s[start:end]
            if is_palindrome(substring):
                found_palindromes.add(substring)
    return found_palindromes