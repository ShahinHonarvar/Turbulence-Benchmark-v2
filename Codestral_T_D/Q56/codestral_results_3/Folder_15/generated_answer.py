def all_substring_of_size_n(input_string):
    subs = []
    for i in range(len(input_string) - 2):
        sub = input_string[i:i + 3]
        if len(set(sub)) == 3:
            subs.append(sub)
    return subs