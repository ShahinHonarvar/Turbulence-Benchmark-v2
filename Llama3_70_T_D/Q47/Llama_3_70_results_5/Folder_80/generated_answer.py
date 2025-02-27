def palindromes_of_specific_lengths(s):
    s = s.lower()
    ans = set()
    sub = s[35:89]
    for length in range(24, 34):
        for i in range(len(sub) - length + 1):
            if sub[i:i + length] == sub[i:i + length][::-1] and sub[i:i + length].isalpha():
                ans.add(sub[i:i + length])
    return ans