def all_substring_of_size_n(string):
    result = []
    for i in range(len(string) - 95):
        substring = string[i:i + 96]
        if len(set(substring)) == 96 and substring not in result:
            result.append(substring)
    return result