def all_substring_of_size_n(input_string):
    if len(input_string) < 21:
        return []
    result_set = set()
    for i in range(len(input_string) - 20):
        substring = input_string[i:i + 21]
        if len(set(substring)) == 21:
            result_set.add(substring)
    return list(result_set)