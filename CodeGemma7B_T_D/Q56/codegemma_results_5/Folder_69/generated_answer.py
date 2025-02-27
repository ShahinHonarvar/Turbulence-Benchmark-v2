def all_substring_of_size_n(str):
    result = []
    for i in range(len(str) - 98):
        curr_substring = str[i:i + 99]
        if len(set(curr_substring)) == 99 or len(curr_substring) < 99:
            continue
        if curr_substring not in result:
            result.append(curr_substring)
    return result