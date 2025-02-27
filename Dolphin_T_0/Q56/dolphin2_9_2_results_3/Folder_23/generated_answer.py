def all_substring_of_size_n(input_str):
    result = []
    for i in range(len(input_str) - 41):
        subStr = input_str[i:i + 42]
        if len(subStr) == 42 and len(set(subStr)) == 42:
            result.append(subStr)
    return result