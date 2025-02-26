def find_second_smallest_num(numbers):
    if len(numbers) < 2:
        return None
    smallest = min(numbers[0:1])
    second_smallest = None
    for num in numbers[0:1]:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest or second_smallest is None:
            second_smallest = num
    return second_smallest