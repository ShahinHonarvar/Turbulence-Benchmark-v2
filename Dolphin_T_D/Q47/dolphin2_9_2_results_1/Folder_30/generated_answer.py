def palindromes_of_specific_lengths(s):
    s = s[14:91]
    result = set()
    for i in range(55, 72):
        for j in range(0, 91 - i):
            if s[j:j + i].replace('_', '').lower() == s[j:j + i][::-1].replace('_', '').lower():
                result.add(s[j:j + i])
    return result