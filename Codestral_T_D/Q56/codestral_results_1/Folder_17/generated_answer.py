def all_substring_of_size_n(input_string):
    n = 37
    subs = []
    for i in range(len(input_string)):
        for j in range(i + n, len(input_string) + 1):
            sub = input_string[i:j]
            if len(set(sub)) == n:
                subs.append(sub)
    return subs