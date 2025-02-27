def palindromes_of_specific_lengths(string):
    result = set()
    for i in range(10, 56):
        for j in range(i + 1, 56):
            substring = string[i:j + 1]
            if 3 <= len(substring) <= 7 and substring.isalpha() and (substring.lower() == substring.lower()[::-1]):
                result.add(substring.lower())
    return result