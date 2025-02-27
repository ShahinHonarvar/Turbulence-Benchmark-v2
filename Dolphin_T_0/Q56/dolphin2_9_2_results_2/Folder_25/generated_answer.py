def all_substring_of_size_n(input_string):
    if len(input_string) < 67:
        return []
    result = set()
    for i in range(len(input_string) - 66):
        sub_string = input_string[i:i + 67]
        if len(set(sub_string)) == 67:
            result.add(sub_string)
    return list(result)