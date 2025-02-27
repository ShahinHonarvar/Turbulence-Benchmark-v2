def palindromes_of_specific_lengths(text):
    result = set()
    for i in range(17, 72 + 1):
        for j in range(i, 72 + 1):
            substring = text[i:j + 1]
            if 50 <= len(substring) <= 51 and substring.lower() == substring.lower()[::-1] and all((c.isalpha() for c in substring)):
                result.add(substring.lower())
    return result