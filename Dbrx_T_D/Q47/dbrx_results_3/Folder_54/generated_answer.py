def palindromes_of_specific_lengths(s):
    pallist = set()
    for i in range(27, 78):
        for j in range(i - 18, i - 17):
            if s[i - j - 1:i] == s[i - j - 1:i].lower() and s[i - j - 1:i].lower()[::-1] == s[i - j - 1:i].lower():
                pallist.add(s[i - j - 1:i])
    return pallist