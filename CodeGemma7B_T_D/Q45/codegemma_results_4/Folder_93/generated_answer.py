def palindromes_between_indices(s):
    result = set()
    str1 = s[2:8] if len(s) >= 8 else ''
    for i in range(len(str1)):
        for j in range(i, len(str1)):
            str2 = ''.join(sorted([ch.lower() for ch in str1[i:j + 1]]))
            if str2 == str2[::-1]:
                result.add(str2)
    return result