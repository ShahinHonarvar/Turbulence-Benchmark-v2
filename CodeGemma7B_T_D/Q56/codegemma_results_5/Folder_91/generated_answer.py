def all_substring_of_size_n(str):
    result = []
    for i in range(len(str) - 5):
        sub_str = str[i:i + 6]
        if sub_str not in result:
            result.append(sub_str)
    return result