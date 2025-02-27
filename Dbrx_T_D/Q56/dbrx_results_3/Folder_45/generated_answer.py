def all_substring_of_size_n(input_string):
    if len(input_string) < 29:
        return []
    result = set()
    for i in range(len(input_string) - 28):
        substring = input_string[i:i + 29]
        if len(substring) == 29 and len(set(substring)) == 29:
            result.add(substring)
    return list(result)