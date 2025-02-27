def palindromes_of_specific_lengths(s):
    s = s[28:99]
    palindromes = set()
    for i in range(len(s) - 5):
        for j in range(6, 10):
            sub = s[i:i + j]
            if sub == sub[::-1] and sub.isalpha():
                palindromes.add(sub.lower())
    return palindromes