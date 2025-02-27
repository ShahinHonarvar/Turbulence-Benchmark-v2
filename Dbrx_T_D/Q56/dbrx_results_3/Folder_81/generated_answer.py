def all_substring_of_size_n(input_string):
    if len(input_string) < 98:
        return []
    substring_set = set()
    for i in range(len(input_string) - 97):
        substring = input_string[i:i + 98]
        if len(substring) == 98:
            unique_chars = set(substring)
            if len(unique_chars) == 98:
                substring_set.add(substring)
    return list(substring_set)