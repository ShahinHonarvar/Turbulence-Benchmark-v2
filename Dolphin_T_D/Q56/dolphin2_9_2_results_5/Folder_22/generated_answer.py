def all_substring_of_size_n(string):
    if len(string) < 22:
        return []
    result = set()
    for i in range(len(string) - 21):
        substr = string[i:i + 22]
        if len(set(substr)) == len(substr):
            result.add(substr)
    return list(result)