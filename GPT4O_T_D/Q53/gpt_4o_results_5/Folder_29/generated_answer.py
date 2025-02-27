def palindrome_of_length_at_least_n(s):

    def is_palindrome(word):
        return word == word[::-1]
    s = ''.join(filter(str.isalpha, s)).lower()
    n = 78
    found_palindromes = set()
    for length in range(n, len(s) + 1):
        for start in range(len(s) - length + 1):
            substring = s[start:start + length]
            if is_palindrome(substring):
                found_palindromes.add(substring)
    return found_palindromes