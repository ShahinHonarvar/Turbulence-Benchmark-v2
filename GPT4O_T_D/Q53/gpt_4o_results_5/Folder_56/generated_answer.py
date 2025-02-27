def palindrome_of_length_at_least_n(s):

    def is_palindrome(subs):
        return subs == subs[::-1]
    s = ''.join(filter(str.isalpha, s)).lower()
    n = 84
    found_palindromes = set()
    for start in range(len(s)):
        for end in range(start + n, len(s) + 1):
            substring = s[start:end]
            if is_palindrome(substring):
                found_palindromes.add(substring)
    return found_palindromes