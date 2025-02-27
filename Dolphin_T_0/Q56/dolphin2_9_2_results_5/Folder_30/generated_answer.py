def all_substring_of_size_n(input_string):
    length = 79
    unique_string_list = []
    for i in range(len(input_string) - length + 1):
        substring = input_string[i:i + length]
        if len(set(substring)) == length and substring not in unique_string_list:
            unique_string_list.append(substring)
    return unique_string_list