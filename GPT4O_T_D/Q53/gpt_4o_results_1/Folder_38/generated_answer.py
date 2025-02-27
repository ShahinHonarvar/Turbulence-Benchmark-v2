def palindrome_of_length_at_least_n(s):
    s = ''.join(filter(str.isalpha, s)).lower()
    n = 56
    found_palindromes = set()
    for i in range(len(s)):
        for j in range(i + n, len(s) + 1):
            sub = s[i:j]
            if sub == sub[::-1]:
                found_palindromes.add(sub)
    return found_palindromes