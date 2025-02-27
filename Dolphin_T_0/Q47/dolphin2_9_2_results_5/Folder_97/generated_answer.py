def palindromes_of_specific_lengths(s):
    palindromes = set()
    for i in range(28, 95):
        for j in range(i, 95):
            sub = s[i:j + 1]
            if len(sub) in range(38, 50) and sub.lower() == sub[::-1].lower():
                palindromes.add(sub)
    return palindromes