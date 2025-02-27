def all_substring_of_size_n(s):
    result = []
    if len(s) < 90:
        return result
    for i in range(len(s) - 89):
        sub_s = s[i:i + 90]
        if len(set(sub_s.replace('\n', ''))) == len(sub_s.replace('\n', '')):
            result.append(sub_s)
    return list(set(result))