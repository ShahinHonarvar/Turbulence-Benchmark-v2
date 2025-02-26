def all_substring_of_size_n(string):
    result = []
    for i in range(len(string) - 87):
        substring = string[i:i + 88]
        if len(set(substring)) == 88 and substring not in result:
            result.append(substring)
    return result