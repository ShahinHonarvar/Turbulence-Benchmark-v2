from math import sqrt, isqrt

def composite_nums_between_indices(num_list):
    start_index = 30
    end_index = 48
    composites = set()
    for i in range(start_index, end_index + 1):
        number = num_list[i]
        if not isqrt(number) == int(sqrt(number)):
            composites.add(number)
    return composites