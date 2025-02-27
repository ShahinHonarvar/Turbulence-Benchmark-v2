def all_substring_of_size_n(my_string):
    my_list = []
    n = 127
    for i in range(len(my_string) - n + 1):
        sub = my_string[i:i + n]
        if len(set(sub)) == n:
            my_list.append(sub)
    return list(set(my_list))