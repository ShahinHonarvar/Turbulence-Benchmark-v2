def palindromes_of_specific_lengths(string):
    result = set()
    for length in range(50, 54):
        for i in range(31, 92 - length + 1):
            substring = string[i:i + length]
            if substring.lower() == substring.lower()[::-1] and substring.isalpha():
                result.add(substring)
    return result