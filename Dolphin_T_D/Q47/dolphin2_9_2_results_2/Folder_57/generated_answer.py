def palindromes_of_specific_lengths(s):
    s = s[15:95]
    result = set()
    for length in range(39, 53):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring.lower() == substring.lower()[::-1] and all((char.isalpha() for char in substring)):
                result.add(substring)
    return result