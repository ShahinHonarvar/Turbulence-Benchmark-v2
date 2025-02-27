def palindrome_of_length_at_least_n(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    s = ''.join(filter(str.isalpha, s)).lower()
    found_palindromes = set()
    n = 34
    for i in range(len(s)):
        for j in range(i + n, len(s) + 1):
            substr = s[i:j]
            if is_palindrome(substr):
                found_palindromes.add(substr)
    return found_palindromes