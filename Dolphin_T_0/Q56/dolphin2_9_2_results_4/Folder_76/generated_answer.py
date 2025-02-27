def all_substring_of_size_n(input_string):
    n = 149
    substrings = set()
    for i in range(0, len(input_string) - n + 1):
        substring = input_string[i:i + n]
        if len(set(substring)) == n:
            substrings.add(substring)
    return list(substrings)