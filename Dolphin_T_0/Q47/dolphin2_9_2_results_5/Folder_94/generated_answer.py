def palindromes_of_specific_lengths(s):
    s = s[40:95]
    result = set()
    for i in range(45, 52):
        for j in range(len(s) - i + 1):
            if s[j:j + i].lower() == s[j:j + i][::-1].lower():
                result.add(s[j:j + i])
    return result