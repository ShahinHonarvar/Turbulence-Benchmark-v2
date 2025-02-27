def all_substring_of_size_n(input_string):
    substrings = set()
    for i in range(len(input_string) - 29):
        current = input_string[i:i + 30]
        if len(set(current)) == 30:
            substrings.add(current)
    return list(substrings)