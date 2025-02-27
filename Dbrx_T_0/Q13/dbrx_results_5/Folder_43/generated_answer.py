def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 86 - 68 + 1:
        return None
    max_num = max(numbers[68:87])
    numbers.remove(max_num)
    second_max_num = max(numbers[68:87])
    if second_max_num < max_num:
        return second_max_num
    else:
        return None