def palindromes_of_specific_lengths(s):
    s = s[11:84]
    result = set()
    for length in range(13, 67):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring.lower() == substring.lower()[::-1] and substring.isalpha():
                result.add(substring)
    return result