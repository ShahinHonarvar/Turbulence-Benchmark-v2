def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 22:
        return None
    min_num = min(numbers[74:96])
    numbers.remove(min_num)
    second_num = min(numbers[74:96])
    if second_num == min_num:
        return None
    else:
        return second_num