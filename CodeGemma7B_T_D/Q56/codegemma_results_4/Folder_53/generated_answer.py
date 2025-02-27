def all_substring_of_size_n(string):
    length = len(string)
    if length < 25:
        return []
    result = set()
    for i in range(length - 24):
        substring = string[i:i + 25]
        result.add(substring)
    return list(result)