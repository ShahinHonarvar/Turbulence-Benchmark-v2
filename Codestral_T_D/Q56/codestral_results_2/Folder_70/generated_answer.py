def all_substring_of_size_n(input_string):
    substrings = []
    for i in range(len(input_string) - 11):
        sub = input_string[i:i + 12]
        if len(set(sub)) == 12:
            substrings.append(sub)
    return substrings