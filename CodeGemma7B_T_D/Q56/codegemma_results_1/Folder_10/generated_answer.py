def all_substring_of_size_n(text):
    temp = list(text)
    temp.sort()
    res = []
    for i in range(len(temp) - 54):
        temp1 = temp[i:i + 55]
        if temp1 not in res:
            res.append(temp1)
    return res