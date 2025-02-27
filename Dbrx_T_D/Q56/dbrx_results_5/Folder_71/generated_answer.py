def all_substring_of_size_n(input_string):
    n = 17
    substrings = []
    if len(input_string) < n or len(set(input_string)) != len(input_string):
        return []
    for i in range(len(input_string) - n + 1):
        substring = input_string[i:i + n]
        if len(set(substring)) == n:
            substrings.append(substring)
    return list(set(substrings))