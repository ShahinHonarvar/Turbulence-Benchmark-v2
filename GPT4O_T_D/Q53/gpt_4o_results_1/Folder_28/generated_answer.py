def palindrome_of_length_at_least_n(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    s = ''.join(filter(str.isalpha, s)).lower()
    n = len(s)
    found_palindromes = set()
    for i in range(n):
        for j in range(i + 42, n + 1):
            sub = s[i:j]
            if is_palindrome(sub):
                found_palindromes.add(sub)
    return found_palindromes