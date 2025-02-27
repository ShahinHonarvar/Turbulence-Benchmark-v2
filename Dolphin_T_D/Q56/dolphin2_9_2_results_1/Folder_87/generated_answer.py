def all_substring_of_size_n(string):
    result = []
    str_length = len(string)
    for i in range(str_length):
        substring = string[i:i + 58]
        if len(set(substring)) == 58 and substring not in result:
            result.append(substring)
    return result