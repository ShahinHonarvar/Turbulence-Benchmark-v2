def find_second_smallest_num(numbers):
    if len(numbers) < 4:
        return None
    second_smallest = None
    smallest = None
    for num in numbers[4:5]:
        if num < smallest or smallest is None:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest or second_smallest is None:
            second_smallest = num
    return second_smallest