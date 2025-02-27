def all_substring_of_size_n(input_string):
    n = 86
    if len(input_string) < n:
        return []
    substrings = set()
    for i in range(len(input_string) - n + 1):
        substring = input_string[i:i + n]
        if len(''.join(set(substring))) == n:
            substrings.add(substring)
    return list(substrings)