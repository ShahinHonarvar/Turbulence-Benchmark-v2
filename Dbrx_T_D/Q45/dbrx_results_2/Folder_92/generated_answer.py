def palindromes_between_indices(s):
    result = set()
    for i in range(4, 8):
        for j in range(i, 8):
            sub_s = s[i:j + 1].lower()
            if len(sub_s) >= 4 and sub_s == sub_s[::-1]:
                result.add(sub_s)
    return result