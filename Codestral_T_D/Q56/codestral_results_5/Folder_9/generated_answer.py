def all_substring_of_size_n(input_string):
    n = 34
    substrings = set()
    for i in range(len(input_string) - n + 1):
        sub = input_string[i:i + n]
        if len(set(sub)) == n:
            substrings.add(sub)
    return list(substrings)