def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    length = len(s)
    for i in range(length):
        for j in range(i + 55, length):
            sub = s[i:j + 1]
            if sub == sub[::-1] and sub.isalpha():
                palindromes.add(sub)
    return palindromes