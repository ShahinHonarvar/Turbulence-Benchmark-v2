def all_substring_of_size_n(string):
    result = set()
    for i in range(len(string) - 78):
        result.add(string[i:i + 79])
    return list(result)