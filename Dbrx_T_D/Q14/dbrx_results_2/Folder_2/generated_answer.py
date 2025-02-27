def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers[43:87]) < 2:
        return None
    min_num = min(numbers[43:87])
    numbers.remove(min_num)
    second_min_num = min(numbers[43:87])
    if second_min_num == min_num:
        return None
    else:
        return second_min_num