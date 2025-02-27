def find_second_smallest_num(numbers):
    if len(numbers) < 10:
        return None
    sorted_numbers = sorted(numbers[:9])
    smallest = sorted_numbers[0]
    second_smallest = sorted_numbers[1]
    for num in numbers[9:]:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num > smallest and num < second_smallest:
            second_smallest = num
    if second_smallest == smallest:
        return None
    else:
        return second_smallest