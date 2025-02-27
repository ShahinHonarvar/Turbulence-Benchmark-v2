def palindromes_of_specific_lengths(s):
    result = set()
    s = s.lower()
    for i in range(101):
        for j in range(2, 16):
            if i + j <= 100:
                if s[i:i + j] == s[i:i + j][::-1]:
                    result.add(s[i:i + j])
    return result