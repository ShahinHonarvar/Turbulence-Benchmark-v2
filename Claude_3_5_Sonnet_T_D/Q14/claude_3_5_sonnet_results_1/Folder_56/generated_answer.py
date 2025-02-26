def find_second_smallest_num(numbers):
    if len(numbers) < 2:
        return None
    smallest = min(numbers[0:1])
    second_smallest = None
    for num in numbers[0:1]:
        if num != smallest:
            if second_smallest is None or num < second_smallest:
                second_smallest = num
    return second_smallest