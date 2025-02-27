def all_substring_of_size_n(input_string):
    if len(input_string) < 25:
        return []
    substrings = set()
    for i in range(len(input_string) - 24):
        substring = input_string[i:i + 25]
        if len(set(substring)) == len(substring):
            substrings.add(substring)
    return list(substrings)