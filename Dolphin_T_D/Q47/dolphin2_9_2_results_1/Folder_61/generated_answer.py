def palindromes_of_specific_lengths(str):
    palindromes = set()
    for i in range(0, 31):
        for j in range(i + 3, 31):
            sub = str[i:j].lower()
            rev_sub = sub[::-1]
            if rev_sub == sub and sub.isalpha() and (len(sub) in range(20, 31)):
                palindromes.add(sub)
    return palindromes