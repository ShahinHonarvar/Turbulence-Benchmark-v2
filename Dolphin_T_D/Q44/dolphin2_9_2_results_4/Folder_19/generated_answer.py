import math

def composite_nums_between_indices(lst):
    output = set()
    for i in range(5, 8):
        number = lst[i]
        if all((number % j != 0 for j in range(2, int(math.sqrt(number)) + 1))):
            output.add(number)
    return output