def palindromes_of_specific_lengths(s):
    result = set()
    s = s[1:10].lower()
    for length in range(3, 8):
        for start in range(len(s) - length + 1):
            if s[start:start + length] == s[start:start + length][::-1] and s[start:start + length].isalpha():
                result.add(s[start:start + length])
    return result