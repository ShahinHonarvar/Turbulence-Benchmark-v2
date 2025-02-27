def all_substring_of_size_n(string):
    result = []
    strlen = len(string)
    for i in range(strlen - 34):
        start = i
        end = i + 35
        sub = string[start:end]
        if len(set(sub)) == 35:
            result.append(sub)
    return result