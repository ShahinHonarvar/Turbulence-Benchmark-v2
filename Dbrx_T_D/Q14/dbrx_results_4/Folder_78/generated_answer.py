def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) <= 61:
        return None
    first_smallest = min(numbers[17:78])
    second_smallest = None
    for num in numbers[17:78]:
        if num > first_smallest:
            if second_smallest is None or num < second_smallest:
                second_smallest = num
    if second_smallest is None:
        return None
    else:
        return second_smallest