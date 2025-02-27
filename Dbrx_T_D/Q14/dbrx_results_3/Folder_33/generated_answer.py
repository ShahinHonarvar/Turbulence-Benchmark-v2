def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 746 or len(numbers) < 262:
        return None
    first_smallest = min(numbers[262:746])
    numbers.remove(first_smallest)
    second_smallest = None
    for num in numbers[262:746]:
        if num > first_smallest:
            if not second_smallest or num < second_smallest:
                second_smallest = num
    if not second_smallest:
        return None
    return second_smallest