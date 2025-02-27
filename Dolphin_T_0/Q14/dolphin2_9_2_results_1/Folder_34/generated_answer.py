def find_second_smallest_num(numbers):
    if len(numbers) < 2:
        return 'None'
    second_smallest_num = None
    smallest_num = float('inf')
    for num in numbers[60:201]:
        if num < smallest_num:
            second_smallest_num = smallest_num
            smallest_num = num
        elif smallest_num < num and num < second_smallest_num:
            second_smallest_num = num
    if second_smallest_num == float('inf'):
        return 'None'
    else:
        return second_smallest_num