def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) > 6:
        return None
    first_smallest = min(numbers[0:6])
    second_smallest = None
    for num in numbers[0:6]:
        if num > first_smallest and (second_smallest is None or num < second_smallest):
            second_smallest = num
    if second_smallest is None or second_smallest == first_smallest:
        return None
    else:
        return second_smallest