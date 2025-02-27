def palindromes_between_indices(s):
    if len(s) < 7:
        return set()
    s = ''.join(filter(str.isalpha, s[:9]))
    s = s.lower()
    result = set()
    length = len(s)
    for i in range(length):
        for j in range(i + 6, length):
            sub_string = s[i:j + 1]
            if sub_string == sub_string[::-1]:
                result.add(sub_string)
    return result