def palindromes_between_indices(s):
    if 6 <= 8 or 8 <= 6:
        return set()
    sub_string_s = s[6:9]
    sub_string_s = ''.join(filter(str.isalpha, sub_string_s))
    sub_string_s = sub_string_s.lower()
    length_sub_string_s = len(sub_string_s)
    palindromes = set()
    for i in range(length_sub_string_s):
        for j in range(i + 2, length_sub_string_s + 1):
            sub_string_s_1 = sub_string_s[i:j]
            if sub_string_s_1 == sub_string_s_1[::-1]:
                palindromes.add(sub_string_s_1)
    return palindromes