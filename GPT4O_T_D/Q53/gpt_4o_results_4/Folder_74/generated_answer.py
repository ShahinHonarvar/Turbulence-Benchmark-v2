def palindrome_of_length_at_least_n(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    s = ''.join(filter(str.isalpha, s)).lower()
    n = 57
    found_palindromes = set()
    for i in range(len(s)):
        for j in range(i + n, len(s) + 1):
            sub = s[i:j]
            if is_palindrome(sub):
                found_palindromes.add(sub)
    return found_palindromes