def all_substring_of_size_n(input_string):
    if len(input_string) < 95:
        return []
    substrings = set()
    for i in range(len(input_string) - 94):
        substring = input_string[i:i + 95]
        if len(set(substring)) == 95:
            substrings.add(substring)
    return list(substrings)