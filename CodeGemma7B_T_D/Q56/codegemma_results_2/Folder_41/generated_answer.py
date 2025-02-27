from itertools import islice

def all_substring_of_size_n(s):
    list = [x for x in islice(s, 74)]
    result = []
    for i in range(len(list)):
        for j in range(i, len(list)):
            if len(set(list[i:j + 1])) == 74:
                result.append(list[i:j + 1])
    return result