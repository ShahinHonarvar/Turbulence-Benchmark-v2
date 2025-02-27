def all_substring_of_size_n(input_string):
    substrings = []
    for i in range(len(input_string)):
        for j in range(i + 114, len(input_string) + 1):
            sub = input_string[i:j]
            if len(set(sub)) == 114:
                substrings.append(sub)
    return substrings