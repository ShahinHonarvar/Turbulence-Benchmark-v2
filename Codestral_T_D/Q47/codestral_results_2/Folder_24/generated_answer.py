def palindromes_of_specific_lengths(s):
    result = set()
    s = s[12:93]
    for length in range(42, 78):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring.isalpha() and substring.lower() == substring[::-1].lower():
                result.add(substring)
    return result