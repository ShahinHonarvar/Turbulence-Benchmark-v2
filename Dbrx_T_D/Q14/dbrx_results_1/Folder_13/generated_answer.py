def find_second_smallest_num(numbers):
    if len(numbers) < 5:
        return None
    min_num = min(numbers[28:33])
    numbers.remove(min_num)
    second_min_num = min(numbers[28:33])
    if second_min_num == min_num:
        return None
    else:
        return second_min_num