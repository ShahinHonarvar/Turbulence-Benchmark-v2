def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers[56:67]) < 2:
        return None
    min_num1 = min(numbers[56:67])
    second_smallest = None
    for num in numbers[56:67]:
        if num == min_num1:
            continue
        if second_smallest is None or num < second_smallest:
            second_smallest = num
    return second_smallest