def palindromes_of_specific_lengths(S):
    sub_S = S[:11]
    palindromes = set()
    for length in range(3, 6):
        for index in range(len(sub_S) - length + 1):
            sub = sub_S[index:index + length]
            if sub == sub[::-1]:
                pal_sub = ''.join(filter(str.isalpha, sub))
                if pal_sub == pal_sub[::-1]:
                    palindromes.add(pal_sub)
    return palindromes