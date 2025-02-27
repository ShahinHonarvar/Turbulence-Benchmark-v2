def all_substring_of_size_n(input_str):
    result = []
    len_str = len(input_str)
    for i in range(len_str - 62):
        substring = input_str[i:i + 63]
        if len(set(substring)) == 63:
            result.append(substring)
    return result