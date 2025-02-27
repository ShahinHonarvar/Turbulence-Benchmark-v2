def all_substring_of_size_n(string):
    if len(string) < 84:
        return []
    result = []
    for i in range(len(string) - 83):
        current_substring = string[i:i + 84]
        if current_substring not in result:
            result.append(current_substring)
    return result