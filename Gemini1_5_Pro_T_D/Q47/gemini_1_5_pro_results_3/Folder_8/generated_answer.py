def palindromes_of_specific_lengths(text):
    result = set()
    for i in range(17, 72 - 49):
        for j in range(i + 49, i + 51):
            substring = text[i:j + 1]
            if len(substring) >= 50 and len(substring) <= 51 and substring.isalpha() and (substring.lower() == substring.lower()[::-1]):
                result.add(substring)
    return result