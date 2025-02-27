def find_second_smallest_num(numbers):
    if len(numbers) < 2:
        return None
    smallest_num = second_smallest_num = float('inf')
    for num in numbers:
        if num < smallest_num:
            second_smallest_num = smallest_num
            smallest_num = num
        elif num < second_smallest_num and num > smallest_num:
            second_smallest_num = num
    return second_smallest_num if second_smallest_num != float('inf') else None