def palindrome_of_length_at_least_n(s):
    s = s.lower()
    length = len(s)
    palindromes = set()
    for i in range(length):
        for j in range(i + 144, length + 1):
            sub = s[i:j]
            if sub == sub[::-1] and sub.isalpha():
                palindromes.add(sub)
    return palindromes