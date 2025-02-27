def all_substring_of_size_n(lst):
    result = []
    for i in range(len(lst) - 130):
        substring = lst[i:i + 130]
        if len(set(substring)) == 130:
            result.append(substring)
    return result