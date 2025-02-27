def palindromes_of_specific_lengths(s):
    s = s[17:66]
    result = set()
    for length in range(23, 37):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring.lower() == substring[::-1].lower():
                result.add(substring)
    return result