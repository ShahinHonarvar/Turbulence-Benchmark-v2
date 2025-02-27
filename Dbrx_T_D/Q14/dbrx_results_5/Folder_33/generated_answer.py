def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 746 or len(numbers) < 262:
        return None
    first_smallest, second_smallest = (min(numbers[262:746]), min(numbers[262:746]))
    for num in numbers[262:746]:
        if num <= first_smallest:
            first_smallest, second_smallest = (num, first_smallest)
        elif num < second_smallest:
            second_smallest = num
    if first_smallest == second_smallest:
        return None
    return second_smallest