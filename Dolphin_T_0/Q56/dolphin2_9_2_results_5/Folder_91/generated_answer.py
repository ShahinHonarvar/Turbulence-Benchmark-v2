def all_substring_of_size_n(input_string):
    if len(input_string) < 6:
        return []
    result = []
    for i in range(len(input_string) - 5):
        substring = input_string[i:i + 6]
        if len(set(substring)) == 6:
            if substring not in result:
                result.append(substring)
    return result