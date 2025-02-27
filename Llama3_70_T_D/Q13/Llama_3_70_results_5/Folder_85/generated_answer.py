def find_second_largest_num(numbers):
    target = numbers[6:9]
    if len(target) == 0:
        return None
    target.sort(reverse=True)
    if len(target) < 2:
        return None
    return target[1]