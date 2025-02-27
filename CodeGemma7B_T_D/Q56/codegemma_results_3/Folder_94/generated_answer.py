def all_substring_of_size_n(str):
    li = []
    for i in range(len(str)):
        for j in range(i + 1, min(len(str), i + 70)):
            ss = str[i:j]
            if ss not in li:
                li.append(ss)
    return li