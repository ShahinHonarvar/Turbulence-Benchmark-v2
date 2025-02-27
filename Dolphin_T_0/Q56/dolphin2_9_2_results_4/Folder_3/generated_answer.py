def all_substring_of_size_n(string):
    if len(string) < 93:
        return []
    result = set()
    for i in range(len(string) - 92):
        if len(set(string[i:i + 93])) == 93:
            result.add(string[i:i + 93])
    return list(result)