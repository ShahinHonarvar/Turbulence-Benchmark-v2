def find_second_smallest_num(numbers):
    if len(numbers) < 2:
        return None
    second_smallest = None
    smallest = min(numbers[8:10])
    for num in numbers[8:10]:
        if num > smallest and (second_smallest is None or num < second_smallest):
            second_smallest = num
    if second_smallest is not None and second_smallest > smallest:
        return second_smallest
    else:
        return None