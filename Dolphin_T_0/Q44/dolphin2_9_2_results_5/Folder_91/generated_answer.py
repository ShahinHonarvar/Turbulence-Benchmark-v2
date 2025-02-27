import math

def composite_nums_between_indices(ints_list):
    result_set = set()
    for i in range(5, 6):
        if i < len(ints_list):
            numbers_between = ints_list[i]
            if numbers_between > 1:
                for j in range(2, int(math.sqrt(numbers_between)) + 1):
                    if numbers_between % j == 0:
                        result_set.add(numbers_between)
                        break
    return result_set