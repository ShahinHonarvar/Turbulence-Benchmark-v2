def all_substring_of_size_n(str):
    result = []
    for i in range(len(str) - 36):
        substring = str[i:i + 37]
        if len(set(substring)) == len(substring):
            result.append(substring)
    return result