def palindromes_of_specific_lengths(s):
    s = s[2:301]
    result = set()
    for length in range(30, 301):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring.lower() == substring.lower()[::-1] and substring.isalpha():
                result.add(substring)
    return result