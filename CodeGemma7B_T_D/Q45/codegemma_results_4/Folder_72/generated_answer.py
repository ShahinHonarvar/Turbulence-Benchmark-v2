def palindromes_between_indices(string):
    english_letters = 'abcdefghijklmnopqrstuvwxyz'
    palindromes = set()
    for i in range(1, 8):
        for j in range(i + 1, 8):
            for k in range(j + 1, 8):
                for l in range(k + 1, 8):
                    for m in range(l + 1, 8):
                        for n in range(m + 1, 8):
                            substring = string[i:n + 1].lower()
                            if substring == substring[::-1] and all((c in english_letters for c in substring)):
                                palindromes.add(substring)
    return palindromes