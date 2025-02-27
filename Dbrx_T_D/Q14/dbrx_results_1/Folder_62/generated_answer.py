def find_second_smallest_num(numbers):
    if len(numbers) < 67:
        return None
    second_smallest = None
    smallest = min(numbers[10:67])
    for num in numbers[10:67]:
        if num == smallest:
            continue
        if second_smallest is None or num < second_smallest:
            second_smallest = num
    return second_smallest