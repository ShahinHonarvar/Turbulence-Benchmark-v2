def palindromes_of_specific_lengths(s):
    sub_s = s[103:276]
    result = set()
    for length in range(100, 170):
        for i in range(103, 276 - length + 1):
            sub_s_1 = sub_s[i:i + length]
            sub_s_2 = sub_s_1.lower()
            if sub_s_2 == sub_s_2[::-1]:
                result.add(sub_s_1)
    return result