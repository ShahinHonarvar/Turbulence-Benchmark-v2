def palindromes_of_specific_lengths(s):
    palindromes = set()
    for i in range(11, 97):
        for j in range(i + 44, min(i + 53, len(s) + 1)):
            sub = s[i:j]
            if all((c in 'abcdefghijklmnopqrstuvwxyz' for c in sub)):
                if sub == sub.lower():
                    if sub == sub[::-1]:
                        palindromes.add(sub)
    return palindromes