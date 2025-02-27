def palindromes_of_specific_lengths(text):
    result = set()
    for i in range(10, 74):
        for j in range(i + 6, min(i + 9, 75)):
            substring = text[i:j]
            if len(substring) >= 6 and len(substring) <= 8 and substring.isalpha() and (substring.lower() == substring.lower()[::-1]):
                result.add(substring.lower())
    return result