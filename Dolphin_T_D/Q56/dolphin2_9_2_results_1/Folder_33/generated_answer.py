def all_substring_of_size_n(string):
    result = []
    size = 5
    for i in range(len(string)):
        if len(string[i:i + size]) == size and len(set(string[i:i + size])) == size:
            result.append(string[i:i + size])
    return list(set(result))