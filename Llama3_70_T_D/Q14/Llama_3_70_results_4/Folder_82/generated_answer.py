def find_second_smallest_num(numbers):
    second_smallest = None
    smallest = float('inf')
    for num in numbers[20:201]:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif second_smallest is None or num < second_smallest:
            second_smallest = num
    return second_smallest