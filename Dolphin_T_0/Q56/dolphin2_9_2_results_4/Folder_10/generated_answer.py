def all_substring_of_size_n(string):
    result = []
    for i in range(len(string)):
        for j in range(i + 55, len(string) + 1):
            substring = string[i:j]
            if len(set(substring)) == len(substring):
                result.append(substring)
    return list(set(result))