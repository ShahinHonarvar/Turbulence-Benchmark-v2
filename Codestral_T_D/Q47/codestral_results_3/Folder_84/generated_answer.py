def palindromes_of_specific_lengths(s):
    s = s[23:78]
    result = set()
    for length in range(13, 41):
        for i in range(len(s) - length + 1):
            sub = s[i:i + length]
            if sub.isalpha() and sub.lower() == sub.lower()[::-1]:
                result.add(sub)
    return result