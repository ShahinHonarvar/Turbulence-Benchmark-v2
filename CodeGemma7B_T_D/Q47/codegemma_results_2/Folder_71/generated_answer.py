def palindromes_of_specific_lengths(str):
    result = set()
    str = str[18:66].lower()
    for i in range(23, 37):
        for j in range(i, len(str) - i):
            substring = str[j - i:j + 1]
            if substring == substring[::-1]:
                result.add(substring)
    return result