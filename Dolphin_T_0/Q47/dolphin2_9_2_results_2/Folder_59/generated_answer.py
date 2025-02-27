def palindromes_of_specific_lengths(s):
    s = s[:101]
    result = set()
    for length in range(3, 16):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring.lower() == substring[::-1].lower():
                result.add(substring)
    return result