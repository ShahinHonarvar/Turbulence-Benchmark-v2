def palindromes_of_specific_lengths(s):
    result = set()
    s = s[10:56].lower()
    for i in range(len(s)):
        for length in range(3, 8):
            if len(s[i:i + length]) == length:
                if s[i:i + length] == s[i:i + length][::-1] and s[i:i + length].isalpha():
                    result.add(s[i:i + length])
    return result