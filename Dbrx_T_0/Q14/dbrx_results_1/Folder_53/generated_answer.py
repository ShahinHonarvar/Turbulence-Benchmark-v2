def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) > 100:
        return None
    min_num = min(numbers[1:100])
    numbers.remove(min_num)
    second_min_num = min(numbers[1:100])
    if second_min_num == min_num:
        return None
    else:
        return second_min_num