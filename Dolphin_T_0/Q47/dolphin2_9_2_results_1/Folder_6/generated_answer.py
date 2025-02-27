def palindromes_of_specific_lengths(s):
    result = set()
    for i in range(45, 99):
        for length in range(40, 48):
            substr = s[i:i + length]
            if set(substr).issubset(set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')) and substr.lower() == substr.lower()[::-1]:
                result.add(substr)
    return result