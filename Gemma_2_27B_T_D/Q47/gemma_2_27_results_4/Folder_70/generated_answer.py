def palindromes_of_specific_lengths(text):
    result = set()
    for i in range(10, 71):
        for j in range(i + 24, min(71, i + 53)):
            substring = text[i:j]
            if substring.isalpha() and substring.lower() == substring.lower()[::-1]:
                result.add(substring)
    return result