def palindromes_of_specific_lengths(s):
    s = s[35:93]
    result = set()
    for length in range(10, 36):
        for i in range(0, len(s) - length + 1):
            if s[i:i + length] == ''.join(reversed(s[i:i + length])) and s[i:i + length].isalpha():
                result.add(s[i:i + length])
    return result