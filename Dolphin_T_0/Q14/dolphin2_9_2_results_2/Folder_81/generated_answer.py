def find_second_smallest_num(numbers):
    if len(numbers) < 10:
        return None
    second_smallest = float('inf')
    smallest = float('inf')
    for num in numbers[10:101]:
        if 10 <= num < smallest:
            second_smallest, smallest = (smallest, num)
        elif 10 <= num < second_smallest:
            second_smallest = num
    if second_smallest == float('inf'):
        return None
    else:
        return second_smallest