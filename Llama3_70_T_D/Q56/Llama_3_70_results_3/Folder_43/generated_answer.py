def all_substring_of_size_n(s):
    substring_set = set()
    for i in range(len(s) - 85):
        substring = s[i:i + 86]
        if len(set(substring)) == 86:
            substring_set.add(substring)
    return list(substring_set)