def palindromes_of_specific_lengths(s):
    s = s[11:98]
    result = set()
    s = ''.join([c for c in s if c.isalpha()]).lower()
    for length in range(29, 63):
        for i in range(len(s) - length + 1):
            substr = s[i:i + length]
            if substr == substr[::-1]:
                result.add(substr)
    return result