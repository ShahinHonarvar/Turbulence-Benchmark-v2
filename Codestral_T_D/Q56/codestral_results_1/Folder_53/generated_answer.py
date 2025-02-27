def all_substring_of_size_n(input_string):
    n = 25
    substrings = []
    for i in range(len(input_string) - n + 1):
        sub = input_string[i:i + n]
        if len(set(sub)) == n:
            substrings.append(sub)
    return substrings