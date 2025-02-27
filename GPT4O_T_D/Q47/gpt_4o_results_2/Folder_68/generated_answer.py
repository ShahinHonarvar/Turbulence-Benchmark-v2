def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    s = ''.join(filter(str.isalpha, s)).lower()
    if len(s) < 51:
        return set()
    palindromes = set()
    for length in range(50, 101):
        for start in range(51):
            if start + length <= 51:
                substring = s[start:start + length]
                if is_palindrome(substring):
                    palindromes.add(substring)
    return palindromes