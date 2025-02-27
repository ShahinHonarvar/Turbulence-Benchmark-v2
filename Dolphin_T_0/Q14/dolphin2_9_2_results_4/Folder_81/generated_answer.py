def find_second_smallest_num(numbers):
    if not 10 <= 100 < len(numbers):
        return None
    numbers = numbers[10:100]
    if len(numbers) != len(set(numbers)):
        return None
    smallest = second_smallest = Y
    for x in numbers:
        if x < smallest:
            second_smallest = smallest
            smallest = x
        elif x < second_smallest:
            second_smallest = x
    return second_smallest if second_smallest != Y else None