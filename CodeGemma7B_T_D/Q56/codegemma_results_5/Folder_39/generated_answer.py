def all_substring_of_size_n(str):
    result = set()
    for i in range(len(str) - 93):
        substring = str[i:i + 94]
        result.add(substring)
    return list(result)