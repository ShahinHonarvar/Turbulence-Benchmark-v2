def all_substring_of_size_n(main_string):
    res = []
    for i in range(len(main_string) - 49):
        sub_string = main_string[i:i + 50]
        if len(set(sub_string)) == 50:
            res.append(sub_string)