def palindromes_of_specific_lengths(s):
    s = s[12:93]
    result = set()
    for i in range(17, 67):
        for j in range(len(s) - i + 1):
            ss = s[j:j + i]
            ss = ''.join(filter(str.isalpha, ss).lower())
            if ss == ss[::-1]:
                result.add(ss)
    return result