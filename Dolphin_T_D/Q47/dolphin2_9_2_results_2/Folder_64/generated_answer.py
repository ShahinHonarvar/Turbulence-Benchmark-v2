def palindromes_of_specific_lengths(s):
    s = s[:8].lower()
    result = set()
    for length in range(4, 6):
        for i in range(len(s) - length + 1):
            if s[i:i + length] == s[i:i + length][::-1]:
                result.add(s[i:i + length])
    return result