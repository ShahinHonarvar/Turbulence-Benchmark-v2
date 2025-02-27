def palindromes_of_specific_lengths(s):
    result = set()
    for i in range(101, 293):
        for j in range(i, 293):
            word = s[i:j + 1]
            if len(word) in range(154, 183):
                word = ''.join((c for c in word if c.isalpha()))
                word = word.lower()
                if word == word[::-1] and word != '':
                    result.add(word)
    return result