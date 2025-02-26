def find_second_smallest_num(numbers):
    if len(numbers) <= 10:
        return None
    slice_numbers = numbers[10:101]
    if len(slice_numbers) < 2:
        return None
    smallest = float('inf')
    second_smallest = float('inf')
    for num in slice_numbers:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest and num != smallest:
            second_smallest = num
    return second_smallest if second_smallest != float('inf') else None