def palindromes_of_specific_lengths(s):
    s = s[103:276]
    result = set()
    for length in range(100, 170):
        for i in range(len(s) - length + 1):
            if s[i:i + length].lower() == s[i:i + length].lower()[::-1] and s[i:i + length].isalpha():
                result.add(s[i:i + length])
    return result