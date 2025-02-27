def all_substring_of_size_n(str):
    result = set()
    for i in range(len(str)):
        for j in range(i + 100, len(str) + 1):
            substring = str[i:j]
            if len(set(substring)) == len(substring):
                result.add(substring)
    return list(result)