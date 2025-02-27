def all_substring_of_size_n(str):
    result = []
    for i in range(len(str) - 98):
        substring = str[i:i + 99]
        if len(set(substring)) == 99:
            result.append(substring)
    return result