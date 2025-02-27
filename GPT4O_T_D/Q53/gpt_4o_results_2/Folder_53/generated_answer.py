def palindrome_of_length_at_least_n(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    s = ''.join(filter(str.isalpha, s)).lower()
    n = 64
    found_palindromes = set()
    for i in range(len(s)):
        for j in range(i + n - 1, len(s)):
            sub = s[i:j + 1]
            if is_palindrome(sub):
                found_palindromes.add(sub)
    return found_palindromes