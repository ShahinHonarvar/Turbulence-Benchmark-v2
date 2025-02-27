def all_substring_of_size_n(input_string):
    if len(input_string) < 52:
        return []
    substrings = set()
    for i in range(len(input_string) - 51):
        substring = input_string[i:i + 52]
        if len(set(substring)) == 52:
            substrings.add(substring)
    return list(substrings)