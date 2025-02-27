def palindromes_of_specific_lengths(s):
    s = s[32:85]
    result = set()
    for length in range(26, 32):
        for i in range(len(s) - length + 1):
            sub = s[i:i + length]
            if sub == sub[::-1] and sub.isalpha():
                result.add(sub.lower())
    return result