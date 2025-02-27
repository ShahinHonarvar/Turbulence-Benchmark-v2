def palindromes_between_indices(s):
    sub_s = s[2:4]
    sub_s = ''.join((ch.lower() for ch in sub_s if ch.isalpha()))
    result = set()
    for i in range(len(sub_s)):
        for j in range(i + 2, len(sub_s) + 1):
            sub_s_2 = sub_s[i:j]
            if sub_s_2 == sub_s_2[::-1] and len(sub_s_2) >= 3:
                result.add(sub_s_2)
    return result