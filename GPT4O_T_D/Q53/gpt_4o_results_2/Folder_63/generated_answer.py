def palindrome_of_length_at_least_n(s):
    s = ''.join(filter(str.isalpha, s)).lower()
    found_palindromes = set()
    length = len(s)
    for i in range(length):
        for j in range(i + 37, length + 1):
            sub = s[i:j]
            if sub == sub[::-1]:
                found_palindromes.add(sub)
    return found_palindromes