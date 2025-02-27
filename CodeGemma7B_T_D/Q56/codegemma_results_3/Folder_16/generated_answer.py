def all_substring_of_size_n(str):
    if len(str) < 124:
        return []
    g = set()
    list_of_unique_substrings = []
    for i in range(len(str)):
        for j in range(i + 124, len(str) + 1):
            substring = str[i:j]
            if len(substring) == 124 and substring not in g:
                list_of_unique_substrings.append(substring)
                g.add(substring)
    return list_of_unique_substrings