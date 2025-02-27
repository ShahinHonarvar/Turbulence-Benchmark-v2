def palindromes_of_specific_lengths(s):
    substring = s[29:96 + 1]
    result = set()
    for length in range(12, 19):
        for i in range(len(substring) - length + 1):
            sub_s = substring[i:i + length]
            sub_s_lower = sub_s.lower()
            if sub_s_lower == sub_s_lower[::-1]:
                result.add(sub_s)
    return result