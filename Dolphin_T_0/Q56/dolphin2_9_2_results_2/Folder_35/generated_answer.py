def all_substring_of_size_n(input_string):
    n = 27
    result = []
    substrings = [input_string[i:i + n] for i in range(len(input_string) - n + 1)]
    for substring in substrings:
        if len(set(substring)) == n and substring not in result:
            result.append(substring)
    return result