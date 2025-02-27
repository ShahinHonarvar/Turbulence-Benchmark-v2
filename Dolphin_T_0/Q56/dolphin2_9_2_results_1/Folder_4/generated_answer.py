def all_substring_of_size_n(input_string):
    subs = {}
    for i in range(len(input_string)):
        cur_string = input_string[i:i + 41]
        if len(set(list(cur_string))) == len(cur_string):
            subs[cur_string] = 1
    return list(subs.keys())