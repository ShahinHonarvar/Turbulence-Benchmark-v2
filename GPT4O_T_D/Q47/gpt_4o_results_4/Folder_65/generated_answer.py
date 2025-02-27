def palindromes_of_specific_lengths(s):
    substr = s[15:96]
    result = set()
    substr = ''.join(filter(str.isalpha, substr)).lower()
    for length in range(20, 67):
        for i in range(len(substr) - length + 1):
            candidate = substr[i:i + length]
            if candidate == candidate[::-1]:
                result.add(s[15:96][i:i + length])
    return result