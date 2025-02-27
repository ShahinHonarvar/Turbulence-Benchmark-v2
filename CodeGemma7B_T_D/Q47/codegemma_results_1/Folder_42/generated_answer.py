def palindromes_of_specific_lengths(string):
    result = set()
    for i in range(43, 96):
        for j in range(i, 96):
            substring = string[i:j + 1]
            if substring.lower() == substring.lower()[::-1] and 17 < len(substring) < 48:
                result.add(substring)
    return result