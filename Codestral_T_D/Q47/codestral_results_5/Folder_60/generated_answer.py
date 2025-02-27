def palindromes_of_specific_lengths(s):
    s = s[23:83]
    result = set()
    for i in range(len(s)):
        for j in range(32, 35):
            if i + j > len(s):
                break
            sub = s[i:i + j]
            if sub.isalpha() and sub.lower() == sub.lower()[::-1]:
                result.add(sub)
    return result