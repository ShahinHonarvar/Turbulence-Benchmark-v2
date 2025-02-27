def palindromes_of_specific_lengths(text):
    result = set()
    for i in range(15, 96):
        for j in range(i + 20, min(i + 67, 96)):
            substring = text[i:j]
            if substring.isalpha() and substring.lower() == substring.lower()[::-1]:
                result.add(substring)
    return result