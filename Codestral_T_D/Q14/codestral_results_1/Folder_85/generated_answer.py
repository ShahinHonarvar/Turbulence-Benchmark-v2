def find_second_smallest_num(numbers):
    if len(numbers) < 2:
        return None
    smallest = min(numbers[0:7])
    second_smallest = float('inf')
    for num in numbers[0:7]:
        if num < second_smallest and num != smallest:
            second_smallest = num
    return None if second_smallest == float('inf') else second_smallest