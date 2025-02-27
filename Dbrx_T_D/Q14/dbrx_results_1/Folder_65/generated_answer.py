def find_second_smallest_num(numbers):
    if len(numbers) < 3:
        return None
    min_num = min(numbers[55:58])
    numbers.remove(min_num)
    second_min_num = min(numbers[55:58])
    return second_min_num if second_min_num > min_num else None