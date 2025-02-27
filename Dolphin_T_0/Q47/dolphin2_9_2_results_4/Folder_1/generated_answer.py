def palindromes_of_specific_lengths(s):
    s = s[14:90].lower()
    result = set()
    for length in range(40, 73):
        for i in range(len(s) - length + 1):
            if s[i:i + length] == s[i:i + length][::-1]:
                result.add(s[i:i + length])
    return result