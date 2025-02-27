def all_substring_of_size_n(input_string):
    substrings = []
    for i in range(len(input_string)):
        for j in range(i + 1, len(input_string) + 1):
            substring = input_string[i:j]
            if len(substring) == 99 and len(set(substring)) == len(substring):
                substrings.append(substring)
    return substrings