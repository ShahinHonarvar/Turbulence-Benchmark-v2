def palindromes_of_specific_lengths(txt):
    result = set()
    for i in range(34, 91):
        for j in range(14, 40):
            substring = txt[i - j:i + j + 1]
            if substring == substring[::-1] and substring.isalpha():
                result.add(substring.lower())
    return result