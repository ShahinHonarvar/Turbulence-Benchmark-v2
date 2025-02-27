def all_substring_of_size_n(input_str):
    n = 45
    substrings = set()
    for i in range(len(input_str) - n + 1):
        substr = input_str[i:i + n]
        if len(set(substr)) == n:
            substrings.add(substr)
    return list(substrings)