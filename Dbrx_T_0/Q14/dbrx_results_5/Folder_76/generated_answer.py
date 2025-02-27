def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 605 or len(numbers) < 533:
        return None
    min_num = min(numbers[533:605])
    numbers.remove(min_num)
    second_min_num = min(numbers[533:605])
    if second_min_num == min_num:
        return None
    else:
        return second_min_num