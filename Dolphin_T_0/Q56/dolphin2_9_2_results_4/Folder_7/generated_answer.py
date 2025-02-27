def all_substring_of_size_n(input_string):
    substrings = []
    for i in range(len(input_string) - 116):
        cur_sub = input_string[i:i + 117]
        if len(set(cur_sub)) == len(cur_sub):
            substrings.append(cur_sub)
    return substrings