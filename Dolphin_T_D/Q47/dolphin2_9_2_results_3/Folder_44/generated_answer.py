def palindromes_of_specific_lengths(s):
    s = s[18:99].lower()
    result = set()
    for i in range(31, 52):
        for j in range(0, len(s) - i + 1):
            if all((c.isalpha() for c in s[j:j + i])) and s[j:j + i] == s[j:j + i][::-1]:
                result.add(s[j:j + i])
    return result