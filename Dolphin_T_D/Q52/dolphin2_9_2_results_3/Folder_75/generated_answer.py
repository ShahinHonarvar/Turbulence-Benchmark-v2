def palindrome_of_length_n(s):
    palindromes = set()
    s = s.lower()
    length = len(s)
    for i in range(length - 79):
        for j in range(i + 79, length):
            sub = s[i:j + 1]
            if sub == sub[::-1]:
                palindromes.add(sub)
    return palindromes