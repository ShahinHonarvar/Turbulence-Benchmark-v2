def find_second_smallest_num(numbers):
    if len(numbers) <= 1:
        return None
    smallest = min(numbers[0:5])
    second_smallest = float('inf')
    for num in numbers[0:5]:
        if num < second_smallest and num != smallest:
            second_smallest = num
    if second_smallest == float('inf'):
        return None
    return second_smallest