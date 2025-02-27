def all_substring_of_size_n(s):
    if len(set(s)) < 87:
        return []
    else:
        length = len(s)
        return [s[i:i + 87] for i in range(length - 86)]