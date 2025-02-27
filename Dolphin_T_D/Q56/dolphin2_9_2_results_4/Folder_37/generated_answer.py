def all_substring_of_size_n(string):
    length_n = 65
    substrings = []
    for i in range(len(string) - length_n + 1):
        sub_string = string[i:i + length_n]
        if len(set(sub_string)) == length_n:
            substrings.append(sub_string)
    return substrings