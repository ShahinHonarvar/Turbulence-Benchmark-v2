def all_substring_of_size_n(my_string):
    substr_set = set()
    n = len(my_string)
    for i in range(n):
        for j in range(i + 130, n + 1):
            substr = my_string[i:j]
            if len(set(substr)) == len(substr):
                substr_set.add(substr)
    return list(substr_set)