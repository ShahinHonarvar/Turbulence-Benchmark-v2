def palindromes_of_specific_lengths(s):
    s = s[29:84]
    s = ''.join((ch for ch in s if ch.isalpha()))
    result = set()
    for length in range(12, 21):
        for i in range(len(s) - length + 1):
            if s[i:i + length].lower() == s[i:i + length].lower()[::-1]:
                result.add(s[i:i + length])
    return result