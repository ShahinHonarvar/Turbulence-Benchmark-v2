def all_substring_of_size_n(input_string):
    n = 12
    substrings = []
    for i in range(len(input_string)):
        if i + n <= len(input_string):
            substring = input_string[i:i + n]
            if len(set(substring)) == n:
                substrings.append(substring)
    return substrings