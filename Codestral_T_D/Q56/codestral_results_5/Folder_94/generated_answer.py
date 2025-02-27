def all_substring_of_size_n(input_string):
    substrings = []
    for i in range(len(input_string) - 69):
        sub = input_string[i:i + 70]
        if len(set(sub)) == 70:
            substrings.append(sub)
    return substrings