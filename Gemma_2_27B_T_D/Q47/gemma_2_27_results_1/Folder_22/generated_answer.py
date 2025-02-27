def palindromes_of_specific_lengths(text):
    result = set()
    for i in range(100, 201):
        for j in range(i + 5, min(i + 11, len(text) + 1)):
            substring = text[i:j]
            if substring.isalpha() and substring.lower() == substring.lower()[::-1]:
                result.add(substring)
    return result