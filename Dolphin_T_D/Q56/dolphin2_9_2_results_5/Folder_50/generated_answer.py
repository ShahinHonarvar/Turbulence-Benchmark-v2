def all_substring_of_size_n(input_string):
    input_string = input_string
    list_of_substrings = []
    length_of_input_string = len(input_string)
    for i in range(length_of_input_string - 10):
        substring = input_string[i:i + 11]
        if len(set(substring)) == 11:
            list_of_substrings.append(substring)
    return list(set(list_of_substrings))