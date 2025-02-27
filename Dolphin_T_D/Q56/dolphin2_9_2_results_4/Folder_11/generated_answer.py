def all_substring_of_size_n(string):
    result = []
    length = len(string)
    if length < 78:
        return result
    for i in range(length - 77):
        substring = string[i:i + 78]
        if len(set(substring)) == len(substring):
            result.append(substring)
    return result