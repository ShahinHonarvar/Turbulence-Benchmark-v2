def find_second_smallest_num(numbers):
    second_smallest = None
    smallest = min(numbers[68:87])
    for num in numbers[68:87]:
        if num > smallest and (second_smallest is None or num < second_smallest):
            second_smallest = num
    return second_smallest