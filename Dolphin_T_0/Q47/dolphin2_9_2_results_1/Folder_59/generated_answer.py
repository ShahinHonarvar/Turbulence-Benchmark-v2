def palindromes_of_specific_lengths(s):
    s = s[:101]
    s = ''.join(filter(str.isalpha, s))
    result = set()
    for length in range(3, 16):
        for i in range(len(s) - length + 1):
            sub = s[i:i + length]
            if sub == sub.lower() and sub == sub[::-1]:
                result.add(sub)
    return result