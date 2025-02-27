def all_substring_of_size_n(input_str):
    if not input_str:
        return []
    size = 45
    result = []
    for i in range(len(input_str) - size + 2):
        substring = input_str[i:i + size]
        if len(set(substring)) == len(substring) == size:
            result.append(substring)
    return result