def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 95 or len(numbers) < 74:
        return None
    min_num = min(numbers[74:96])
    numbers.append(min_num)
    second_smallest_num = min(set(numbers[74:96]) - {min_num})
    if second_smallest_num == min_num:
        return None
    else:
        return second_smallest_num