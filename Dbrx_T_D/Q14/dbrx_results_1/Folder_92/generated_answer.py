def find_second_smallest_num(numbers):
    if len(numbers) < 2:
        return None
    min_num, second_min_num = (numbers[0], numbers[1]) if numbers[0] < numbers[1] else (numbers[1], numbers[0])
    for num in numbers[2:]:
        if num < min_num:
            second_min_num, min_num = (min_num, num)
        elif num < second_min_num and num != min_num:
            second_min_num = num
    return None if min_num == second_min_num else second_min_num