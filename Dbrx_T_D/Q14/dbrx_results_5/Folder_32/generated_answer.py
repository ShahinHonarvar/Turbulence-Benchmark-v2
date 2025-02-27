def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 36:
        return None
    numbers_to_check = numbers[31:36]
    if len(numbers_to_check) < 2:
        return None
    first_smallest, second_smallest = (min(numbers_to_check[:2]), max(numbers_to_check[:2]))
    for num in numbers_to_check[2:]:
        if num < first_smallest:
            first_smallest, second_smallest = (num, first_smallest)
        elif num > first_smallest and num < second_smallest:
            second_smallest = num
    if second_smallest == first_smallest:
        return None
    return second_smallest