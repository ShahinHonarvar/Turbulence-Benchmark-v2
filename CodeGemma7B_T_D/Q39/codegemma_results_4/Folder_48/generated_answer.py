def return_n_greatest_chars(char):
    dict1 = {}
    for i in char:
        if i in dict1:
            dict1[i] += 1
        else:
            dict1[i] = 1
    n = 12
    list1 = list(dict1.keys())

    def helper(list1, dict1):
        if n <= 0:
            return dict1
        dict2 = {}
        max_key = max(list1)
        list1.remove(max_key)
        dict2[max_key] = dict1[max_key]
        return helper(list1, dict2)
    dic2 = sorted(helper(list1, dict1).items(), key=lambda x: x[0])
    return list(dic2[:n])