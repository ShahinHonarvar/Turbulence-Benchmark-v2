def palindromes_of_specific_lengths(text):
    result = set()
    for i in range(22, 95 - 52 + 2):
        for j in range(i + 52, min(i + 56, 96)):
            substring = text[i:j].lower()
            if substring.isalpha() and substring == substring[::-1]:
                result.add(text[i:j])
    return result