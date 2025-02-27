def all_substring_of_size_n(input_str):
    dist_subs = set()
    str_length = len(input_str)
    for i in range(0, str_length - 78):
        sub = input_str[i:i + 79]
        if len(set(sub)) == 79:
            dist_subs.add(sub)
    return list(dist_subs)