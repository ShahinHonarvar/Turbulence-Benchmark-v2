def find_second_smallest_num(numbers):
    if len(numbers) < 2:
        return None
    smallest = second_smallest = float('inf')
    for n in numbers[:7]:
        if n <= smallest:
            second_smallest = smallest
            smallest = n
        elif n < second_smallest:
            second_smallest = n
    return None if second_smallest == float('inf') else second_smallest