def all_substring_of_size_n(input_string):
    substrings = set()
    for i in range(len(input_string) - 80):
        substring = input_string[i:i + 81]
        if len(set(substring)) == 81:
            substrings.add(substring)
    return list(substrings)