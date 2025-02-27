def find_second_smallest_num(numbers):
    if len(numbers) < 2:
        return None
    smallest = numbers[0]
    second_smallest = None
    for num in numbers:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest or second_smallest is None:
            second_smallest = num
    return second_smallest