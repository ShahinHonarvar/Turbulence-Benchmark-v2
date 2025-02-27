def all_substring_of_size_n(string):
    length = len(string)
    result = []
    for i in range(length - 21):
        substring = string[i:i + 22]
        if len(set(substring)) == 22:
            result.append(substring)
    result = list(set(result))
    return result