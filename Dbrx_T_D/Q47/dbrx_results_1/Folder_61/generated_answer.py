def palindromes_of_specific_lengths(s):
    result = set()
    s = s.lower()
    for i in range(31):
        for j in range(20, 31):
            if i + j <= len(s) and s[i:i + j] == s[i:i + j][::-1]:
                result.add(s[i:i + j])
    return result