def palindromes_of_specific_lengths(text):
    result = set()
    for i in range(119, 257):
        for j in range(i, 257):
            substring = text[i:j + 1]
            if len(substring) >= 104 and len(substring) <= 123 and substring.isalpha() and (substring.lower() == substring.lower()[::-1]):
                result.add(substring.lower())
    return result