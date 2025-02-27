def all_substring_of_size_n(input_string):
    n = 90
    substrings = []
    for i in range(len(input_string)):
        for j in range(i + n, len(input_string) + 1):
            substring = input_string[i:j]
            if len(set(substring)) == n and substring not in substrings:
                substrings.append(substring)
    return substrings