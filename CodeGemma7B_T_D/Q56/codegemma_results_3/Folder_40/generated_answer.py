def all_substring_of_size_n(str):
    substring = set()
    for i in range(len(str) - 1):
        substring.add(str[i] + str[i + 1])
    if substring:
        return list(substring)
    else:
        return []