def palindromes_of_specific_lengths(s):
    palindromes = set()
    for i in range(10, 76):
        for j in range(i + 2, 77):
            sub = s[i:j].lower()
            if sub == sub[::-1] and 10 <= len(sub) <= 20 and sub.isalpha():
                palindromes.add(sub)
    return palindromes