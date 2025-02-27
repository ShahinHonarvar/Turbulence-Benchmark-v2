def palindromes_of_specific_lengths(s):
    sub_s = s[10:101].lower()
    result_set = set()
    for length in range(10, 51):
        for start_point in range(0, len(sub_s) - length + 1):
            sr = sub_s[start_point:start_point + length]
            if set(sr) <= set('abcdefghijklmnopqrstuvwxyz'):
                if sr == sr[::-1]:
                    result_set.add(sr)
    return result_set