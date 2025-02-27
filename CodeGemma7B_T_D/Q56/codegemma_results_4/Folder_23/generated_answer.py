from itertools import combinations

def all_substring_of_size_42(str):
    list = [''.join(i) for i in combinations(str, 42)]
    for i in range(len(list)):
        if len(set(list[i])) != 42:
            list[i] = 'dummy'
    list = [x for x in list if x != 'dummy']
    return list