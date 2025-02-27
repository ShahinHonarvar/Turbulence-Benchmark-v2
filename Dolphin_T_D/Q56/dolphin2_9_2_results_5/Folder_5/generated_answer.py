def all_substring_of_size_n(string):
    result = []
    for i in range(0, len(string) - 63):
        substring = string[i:i + 64]
        if len(set(substring)) == 64:
            if substring not in result:
                result.append(substring)
    return result