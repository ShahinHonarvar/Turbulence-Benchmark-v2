def palindromes_of_specific_lengths(s):
    s = s[14:91]
    result = set()
    for length in range(55, 72):
        for i in range(len(s) - length + 1):
            sub = s[i:i + length]
            sub = ''.join(filter(str.isalpha, sub)).lower()
            if sub == sub[::-1]:
                result.add(sub)
    return result