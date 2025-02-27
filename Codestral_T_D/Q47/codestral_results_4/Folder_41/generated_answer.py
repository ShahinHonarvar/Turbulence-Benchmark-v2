def palindromes_of_specific_lengths(s):
    s = s[1:8]
    s = s.lower()
    result = set()
    for i in range(len(s)):
        for j in range(i + 3, i + 5):
            if j < len(s) and s[i:j] == s[j:i:-1] and s[i:j].isalpha():
                result.add(s[i:j])
    return result