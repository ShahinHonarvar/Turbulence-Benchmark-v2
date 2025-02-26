def all_substring_of_size_n(string):
    result = set()
    for i in range(len(string) - 37):
        substring = string[i:i + 38]
        if len(set(substring)) == 38:
            result.add(substring)
    return list(result)