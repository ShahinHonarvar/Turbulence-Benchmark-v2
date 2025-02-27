from math import sqrt

def composite_nums_between_indices(int_list):
    composites = []
    for i in range(62, 93):
        if int_list[i] > 1 and int_list[i] != 2 and (int_list[i] != 3):
            for j in range(2, int(sqrt(int_list[i])) + 1):
                if int_list[i] % j == 0:
                    composites.append(int_list[i])
                    break
    return set(composites if composites else [])