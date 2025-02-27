def palindromes_of_specific_lengths(s):
    result = set()
    s = s[30:96]
    for length in range(34, 56):
        for i in range(len(s) - length + 1):
            sub = s[i:i + length]
            if sub.lower() == sub.lower()[::-1] and all((c.isalpha() for c in sub)):
                result.add(sub)
    return result