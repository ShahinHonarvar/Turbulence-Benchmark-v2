def is_composite(number):
    if number < 4:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return True
    return False

def composite_nums_between_indices(lst):
    composites = set()
    for index in range(19, 93):
        if index < len(lst) and is_composite(lst[index]):
            composites.add(lst[index])
    return composites