def all_substring_of_size_n(s):
    if len(s) < 127:
        return []
    else:
        list_substring = []
        for i in range(len(s) - 126):
            substring = s[i:i + 127]
            if len(set(substring)) == 127:
                list_substring.append(substring)
        return list_substring