def all_substring_of_size_n(s):
    substr_list = []
    n = 40
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if len(set(substring)) == n:
            substr_list.append(substring)
    return list(set(substr_list))