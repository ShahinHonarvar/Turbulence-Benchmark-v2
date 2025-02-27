def all_substring_of_size_n(input_string):
    size = 41
    if len(input_string) < size:
        return []
    result_set = set()
    for i in range(len(input_string) - size + 1):
        substring = input_string[i:i + size]
        if len(set(substring)) == size:
            result_set.add(substring)
    return list(result_set)