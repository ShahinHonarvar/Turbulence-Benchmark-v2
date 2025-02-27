def all_substring_of_size_n(str):
    result = []
    for i in range(len(str) - 143 + 1):
        substring = str[i:i + 143]
        if substring not in result:
            result.append(substring)
    return result