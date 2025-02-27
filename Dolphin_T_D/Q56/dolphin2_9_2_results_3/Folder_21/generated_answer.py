def all_substring_of_size_n(s):
    result = []
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            sub_s = s[i:j]
            if len(sub_s) == 106 and len(set(sub_s)) == len(sub_s):
                result.append(sub_s)
    return result