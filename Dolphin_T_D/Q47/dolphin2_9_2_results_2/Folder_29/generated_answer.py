def palindromes_of_specific_lengths(s):
    s = s[15:95]
    result = set()
    for length in range(18, 74):
        for i in range(len(s) - length + 1):
            if s[i:i + length].lower() == s[i:i + length].lower()[::-1] and s[i:i + length].isalpha():
                result.add(s[i:i + length])
    return result