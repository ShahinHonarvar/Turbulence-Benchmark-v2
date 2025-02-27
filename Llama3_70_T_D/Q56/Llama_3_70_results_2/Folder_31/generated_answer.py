def all_substring_of_size_n(s):
    substring_set = set()
    for i in range(len(s) - 45):
        substring = s[i:i + 46]
        if len(set(substring)) == 46:
            substring_set.add(substring)
    return list(substring_set)