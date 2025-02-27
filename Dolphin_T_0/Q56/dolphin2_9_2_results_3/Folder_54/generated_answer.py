def all_substring_of_size_n(input_string):
    n = 28
    list_substr = []
    for i in range(len(input_string) - n + 1):
        substring = input_string[i:i + n]
        if substring in list_substr:
            continue
        if len(set(substring)) == n:
            list_substr.append(substring)
    return list_substr