def all_substring_of_size_n(string):
    result = []
    for i in range(len(string) - 143 + 1):
        substring = string[i:i + 143]
        if len(set(substring)) == 143:
            result.append(substring)
    return set(result)