def all_substring_of_size_n(s):
    n = len(s)
    substr_list = []
    for i in range(n - 8):
        if len(set(s[i:i + 90])) == 90:
            substr_list.append(''.join(s[i:i + 90]))
    return list(set(substr_list))