def all_substring_of_size_n(string):
    length = len(string)
    result = []
    for i in range(length - 26):
        temp = string[i:i + 27]
        if len(set(temp)) == len(temp):
            result.append(temp)
    return list(set(result))