def all_substring_of_size_n(string):
    result = set()
    for i in range(len(string) - 66):
        substring = string[i:i + 67]
        if len(set(substring)) == 67:
            result.add(substring)
    return list(result)