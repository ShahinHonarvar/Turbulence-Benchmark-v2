def all_substring_of_size_n(input_string):
    size = 4
    all_substrings = set()
    if len(input_string) < size:
        return []
    for i in range(len(input_string) - size + 1):
        current_substring = input_string[i:i + size]
        if len(set(current_substring)) == size:
            all_substrings.add(current_substring)
    if not all_substrings:
        return []
    return list(all_substrings)