def all_substring_of_size_n(str):
    for i in range(len(str) - 33):
        s = str[i:i + 34]
        if len(set(s)) == len(s):
            print(s)