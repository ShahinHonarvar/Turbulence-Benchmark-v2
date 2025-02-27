def all_substring_of_size_n(input_string):
    if len(input_string) < 19:
        return []
    unique_substrs = set()
    for i in range(len(input_string) - 18):
        substring = input_string[i:i + 19]
        unique_substrs.add(substring)
    return list(unique_substrs)