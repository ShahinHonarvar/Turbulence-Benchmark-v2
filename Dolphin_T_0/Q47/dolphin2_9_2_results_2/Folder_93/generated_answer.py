def palindromes_of_specific_lengths(s):
    s = s[16:96].lower()
    res = set()
    for length in range(13, 50):
        for i in range(len(s) - length + 1):
            if s[i:i + length] == s[i:i + length][::-1] and s[i:i + length].isalpha():
                res.add(s[i:i + length])
    return res