def all_substring_of_size_n(input_string):
    result = set()
    for i in range(len(input_string) - 60):
        substring = input_string[i:i + 61]
        if len(set(substring)) == 61:
            result.add(substring)
    return list(result)