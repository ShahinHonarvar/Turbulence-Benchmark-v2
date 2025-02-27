def all_substring_of_size_n(input_str):
    n = 117
    result = []
    if len(input_str) < n:
        return result
    for i in range(len(input_str) - n + 1):
        substring = input_str[i:i + n]
        if len(set(substring)) == n:
            result.append(substring)
    return result