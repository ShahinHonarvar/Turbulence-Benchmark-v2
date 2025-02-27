def palindromes_of_specific_lengths(s):
    s = s[0:101]
    result = set()
    for length in range(3, 16):
        for i in range(0, 101 - length + 1):
            if s[i:i + length].lower() == s[i:i + length].lower()[::-1]:
                result.add(s[i:i + length])
    return result