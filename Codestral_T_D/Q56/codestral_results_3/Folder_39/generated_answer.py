def all_substring_of_size_n(input_string):
    n = 94
    substrings = []
    for i in range(len(input_string)):
        for j in range(i + n, len(input_string) + 1):
            substring = input_string[i:j]
            if len(set(substring)) == n:
                substrings.append(substring)
    return substrings