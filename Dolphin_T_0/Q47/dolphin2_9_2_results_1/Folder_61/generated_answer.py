def palindromes_of_specific_lengths(s):
    sub_s = s[0:30].lower()
    result = set()
    for length in range(20, 31):
        for i in range(len(sub_s) - length + 1):
            sub_s_i = sub_s[i:i + length]
            if sub_s_i == sub_s_i[::-1] and sub_s_i.isalpha():
                result.add(sub_s_i)
    return result