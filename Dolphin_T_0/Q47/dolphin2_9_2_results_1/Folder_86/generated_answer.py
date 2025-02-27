def palindromes_of_specific_lengths(s):
    s = s[29:95]
    result = set()
    for length in range(34, 56):
        for i in range(len(s)):
            if s[i:i + length].lower() == s[i:i + length].lower()[::-1] and s[i:i + length].isalpha():
                result.add(s[i:i + length])
    return result