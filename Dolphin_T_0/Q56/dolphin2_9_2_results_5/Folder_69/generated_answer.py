def all_substring_of_size_n(input_str):
    result = []
    len_input = len(input_str)
    if len_input < 99:
        return result
    for i in range(0, len_input - 98):
        substring = input_str[i:i + 99]
        substring_set = set(substring)
        if len(substring_set) == 99:
            result.append(substring)
    return result