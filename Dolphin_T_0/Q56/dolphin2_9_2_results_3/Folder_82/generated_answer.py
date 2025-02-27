def all_substring_of_size_n(input_string):
    length = len(input_string)
    if length < 100:
        return []
    substr_set = set()
    for i in range(length - 99):
        substring = input_string[i:i + 100]
        if len(set(substring)) == 100:
            substr_set.add(substring)
    return list(substr_set)