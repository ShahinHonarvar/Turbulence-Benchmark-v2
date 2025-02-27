def palindromes_of_specific_lengths(s):
    subs = s[100:201]
    subs = ''.join(filter(str.isalpha, subs)).lower()
    res = set()
    for i in range(len(subs) - 4):
        for j in range(i + 5, len(subs) + 1):
            if 5 <= j - i <= 10 and subs[i:j] == subs[i:j][::-1]:
                res.add(subs[i:j])
    return res