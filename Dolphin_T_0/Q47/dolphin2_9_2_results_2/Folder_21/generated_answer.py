def palindromes_of_specific_lengths(s):
    s = s[100:296]
    palindromes = set()
    for i in range(136, 161):
        for j in range(len(s) - i + 1):
            sub = s[j:j + i].lower()
            if sub == sub[::-1] and sub.isalpha():
                palindromes.add(sub)
    return palindromes