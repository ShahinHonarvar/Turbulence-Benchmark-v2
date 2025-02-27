def palindromes_of_specific_lengths(s):
    s = s[22:96]
    result = set()
    for length in range(52, 56):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring.isalpha() and substring.lower() == substring[::-1].lower():
                result.add(substring)
    return result