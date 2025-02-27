def all_substring_of_size_n(str_input):
    if len(str_input) < 19:
        return []
    result = set()
    for i in range(len(str_input) - 18):
        substring = str_input[i:i + 19]
        result.add(substring)
    return list(result)