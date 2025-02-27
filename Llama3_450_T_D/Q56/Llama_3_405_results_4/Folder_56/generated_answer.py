def all_substring_of_size_n(input_string):
    result = set()
    for i in range(len(input_string) - 68):
        substring = input_string[i:i + 69]
        if len(set(substring)) == 69:
            result.add(substring)
    return list(result)