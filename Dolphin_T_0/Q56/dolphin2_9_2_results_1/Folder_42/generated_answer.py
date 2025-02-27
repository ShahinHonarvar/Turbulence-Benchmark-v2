def all_substring_of_size_n(input_string):
    if len(input_string) < 45:
        return []
    result = []
    for i in range(len(input_string) - 44):
        substring = input_string[i:i + 45]
        if len(set(substring)) == 45:
            result.append(substring)
    return result