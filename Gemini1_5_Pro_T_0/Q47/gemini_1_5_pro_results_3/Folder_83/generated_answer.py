def palindromes_of_specific_lengths(text):
    result = set()
    for i in range(75, 96):
        for j in range(i + 7, min(i + 10, 96 + 1)):
            substring = text[i:j].lower()
            if substring.isalpha() and substring == substring[::-1]:
                result.add(substring)
    return result