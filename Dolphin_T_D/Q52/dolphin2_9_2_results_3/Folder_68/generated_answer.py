def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 75):
        for j in range(i + 76, len(s) + 1):
            sub = s[i:j]
            if all((x.isalpha() for x in sub)) and sub == sub[::-1]:
                palindromes.add(sub)
    return palindromes