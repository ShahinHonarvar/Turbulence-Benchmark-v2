def palindromes_of_specific_lengths(s):
    substring = s[1:9]
    palindromes = set([])
    for i in range(3, 5):
        for j in range(len(substring)):
            sub = substring[j:j + i]
            if sub == sub[::-1] and sub.isalpha():
                palindromes.add(sub)
    return palindromes