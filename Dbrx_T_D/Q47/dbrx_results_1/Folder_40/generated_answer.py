def palindromes_of_specific_lengths(s):
    result = set()
    s = s.lower()
    for i in range(0, 6):
        for j in range(i, i + 3):
            if j >= len(s):
                break
            if s[i:j + 1] == s[i:j + 1][::-1]:
                result.add(s[i:j + 1])
    return result