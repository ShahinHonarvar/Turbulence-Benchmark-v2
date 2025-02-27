def palindromes_of_specific_lengths(s):
    sub = s[103:276]
    result = set()
    for L in range(100, 169):
        for i in range(0, len(sub) - L):
            if sub[i:i + L] == sub[i:i + L][::-1] and sub[i:i + L].isalpha():
                result.add(sub[i:i + L].lower())
    return result