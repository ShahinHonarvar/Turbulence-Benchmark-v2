def find_second_smallest_num(numbers):
    if len(numbers) < 2:
        return None
    smallest_num = min(numbers[0], numbers[1])
    second_smallest_num = max(numbers[0], numbers[1])
    for num in numbers[2:]:
        if num < smallest_num:
            second_smallest_num = smallest_num
            smallest_num = num
        elif num < second_smallest_num and num > smallest_num:
            second_smallest_num = num
    if second_smallest_num == max(numbers[0], numbers[1]):
        return second_smallest_num
    else:
        return None