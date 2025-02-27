def palindromes_between_indices(string):
    letters = set()
    for i in range(1, 5):
        if string[i].isalpha():
            letters.add(string[i].lower())
    palindromes = set()
    for i in letters:
        for j in letters:
            for k in letters:
                for l in letters:
                    temp = i + j + k + l
                    if len(temp) >= 4 and temp == temp[::-1]:
                        palindromes.add(temp)
    return palindromes