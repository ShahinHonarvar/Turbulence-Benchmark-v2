def all_substring_of_size_n(input_string):
    if len(input_string) < 37:
        return []
    distinct_substrings = set()
    for i in range(len(input_string) - 36):
        substring = input_string[i:i + 37]
        if len(set(substring)) == 37:
            distinct_substrings.add(substring)
    return list(distinct_substrings)