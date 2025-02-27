def all_substring_of_size_n(s):
    list = set()
    for i in range(len(s)):
        for j in range(i + 144, len(s) + 1):
            str = s[i:j]
            if len(set(str)) < 40:
                continue
            list.add(str)
    return list