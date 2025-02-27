from itertools import permutations

def palindromes_between_indices(s):
    str_obj = list(s.upper())[1:9]
    my_set = set()
    for i in range(2, len(str_obj) + 1):
        obj = permutations(str_obj, i)
        for j in list(obj):
            temp = list(j)
            temp.sort()
            my_set.add(''.join(temp))
    if len(my_set) == 0:
        return set()
    else:
        return my_set