def palindromes_of_specific_lengths(s):
    substr = s[30:96]
    res = set()
    n = len(substr)
    for length in range(34, 56):
        if length > n:
            break
        for i in range(n - length + 1):
            segment = substr[i:i + length]
            letters_only = ''.join(filter(str.isalpha, segment)).lower()
            if letters_only == letters_only[::-1]:
                res.add(segment)
    return res