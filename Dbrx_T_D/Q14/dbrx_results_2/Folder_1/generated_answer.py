def find_second_smallest_num(numbers):
    if len(numbers[34:56]) < 2:
        return None
    first_smallest = min(numbers[34], numbers[35])
    second_smallest = float('inf')
    for num in numbers[34:56]:
        if num > first_smallest and num < second_smallest:
            second_smallest = num
    return second_smallest if second_smallest != float('inf') else None