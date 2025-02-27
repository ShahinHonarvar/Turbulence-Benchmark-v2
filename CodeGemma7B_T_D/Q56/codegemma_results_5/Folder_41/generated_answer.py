def all_substring_of_size_n(text):
    lst = []
    for i in range(len(text)):
        for j in range(i, len(text)):
            lst.append(text[i:j + 1])
    uni_lst = []
    for i in lst:
        if len(i) == 74 and len(set(i)) == 74:
            uni_lst.append(i)
    return uni_lst