def all_substring_of_size_n(input_string):
    n = 47
    result = set()
    for i in range(len(input_string) - n + 1):
        sub_string = input_string[i:i + n]
        if len(set(list(sub_string))) == n:
            result.add(sub_string)
    return list(result)