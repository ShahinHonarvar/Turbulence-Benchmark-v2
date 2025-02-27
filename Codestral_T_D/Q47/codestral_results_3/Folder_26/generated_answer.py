def palindromes_of_specific_lengths(s):
    result = set()
    for length in range(21, 32):
        for i in range(24, 85 - length + 1):
            sub = s[i:i + length]
            if sub.isalpha() and sub.lower() == sub.lower()[::-1]:
                result.add(sub)
    return result