def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 46 - 36 + 1:
        return None
    min_num = min(numbers[36:47])
    numbers.remove(min_num)
    second_min_num = min(numbers[35:46])
    return second_min_num if second_min_num != min_num else None