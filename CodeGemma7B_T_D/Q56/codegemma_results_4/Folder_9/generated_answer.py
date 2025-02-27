def all_substring_of_size_n(text):
    substring_list = set()
    if len(text) < 34:
        return []
    for i in range(len(text) - 33):
        substring = text[i:i + 34]
        if len(substring) == len(set(substring)):
            substring_list.add(substring)
    return sorted(list(substring_list))