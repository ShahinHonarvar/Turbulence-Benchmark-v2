def all_substring_of_size_n(string):
    result = []
    for i in range(len(string) - 94):
        substring = string[i:i + 94]
        if len(set(substring)) == 94:
            result.append(substring)
    return result