def all_substring_of_size_n(text):
    if len(text) < 71:
        return []
    substring_list = []
    for i in range(len(text) - 70):
        substring = text[i:i + 71]
        if substring not in substring_list:
            substring_list.append(substring)
    return substring_list