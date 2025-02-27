def all_substring_of_size_n(input_string):
    result = list()
    for i in range(len(input_string) - 148):
        test_substring = input_string[i:i + 149]
        if len(set(test_substring)) == 149:
            result.append(test_substring)
    return result