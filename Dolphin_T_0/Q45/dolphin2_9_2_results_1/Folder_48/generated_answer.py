def palindromes_between_indices(s):
    sub_str = s[6:9]
    palindromes = set()
    for i in range(4, len(sub_str) + 1):
        for comb in combinations(sub_str, i):
            word = ''.join(comb)
            if word == word[::-1]:
                palindromes.add(word.lower())
    return palindromes if palindromes else set()