def palindromes_between_indices(str):
    str = str.lower()
    palindromes = set()
    for i in range(5, 10):
        for j in range(i + 1, 10):
            for k in range(j + 1, 10):
                for l in range(k + 1, 10):
                    for m in range(l + 1, 10):
                        letters = str[i:m + 1]
                        if letters == letters[::-1]:
                            palindromes.add(letters)
    return palindromes