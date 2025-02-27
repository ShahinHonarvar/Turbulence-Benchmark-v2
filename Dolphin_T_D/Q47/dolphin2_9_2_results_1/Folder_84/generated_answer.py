def palindromes_of_specific_lengths(s):
    s = s[23:78].lower()
    result = set()
    for i in range(13, 41):
        for j in range(len(s) - i + 1):
            if s[j:j + i] == s[j:j + i][::-1] and s[j:j + i].isalpha():
                result.add(s[j:j + i])
    return result