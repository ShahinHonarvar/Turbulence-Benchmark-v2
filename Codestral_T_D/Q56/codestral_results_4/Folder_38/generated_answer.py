def all_substring_of_size_n(input_string):
    substrings = []
    length = len(input_string)
    for i in range(length - 34):
        sub = input_string[i:i + 35]
        if len(set(sub)) == 35:
            substrings.append(sub)
    return substrings