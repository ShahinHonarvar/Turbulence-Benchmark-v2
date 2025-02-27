def all_substring_of_size_n(str):
    result_list = []
    result_set = set()
    for i in range(len(str)):
        for j in range(i + 90, len(str) + 1):
            substring = str[i:j]
            if len(set(substring)) == 90 and substring not in result_set:
                result_set.add(substring)
                result_list.append(substring)
    return result_list