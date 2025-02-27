def palindromes_between_indices(string):
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    palindromes = set()
    for i in range(5, 8):
        for j in range(i + 1, 8):
            for k in range(j + 1, 8):
                for l in range(k + 1, 8):
                    substring = string[i:j + 1] + string[l] + string[k] + string[j] + string[i:j + 1]
                    if substring.lower() in english_letters:
                        palindromes.add(substring.lower())
    return palindromes