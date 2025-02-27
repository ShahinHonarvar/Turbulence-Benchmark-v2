def all_substring_of_size_n(s):
    length = len(s)
    if length < 117:
        return []
    sub_strings = []
    seen = set()
    for i in range(length - 117):
        sub_str = s[i:i + 117]
        if len(set(sub_str)) == len(sub_str):
            if sub_str not in seen:
                seen.add(sub_str)
                sub_strings.append(sub_str)
    return sub_strings