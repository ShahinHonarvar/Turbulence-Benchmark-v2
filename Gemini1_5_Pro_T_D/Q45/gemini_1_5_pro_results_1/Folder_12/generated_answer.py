def palindromes_between_indices(string):
    s = string[3:9].lower()
    letters = set(filter(str.isalpha, s))
    palindromes = set()
    for i in letters:
        for j in letters:
            for k in letters:
                for l in letters:
                    word = i + j + k + l
                    if word == word[::-1]:
                        palindromes.add(word)
    return palindromes