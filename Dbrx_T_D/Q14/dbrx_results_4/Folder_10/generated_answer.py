def find_second_smallest_num(numbers):
    if len(numbers) < 3 or len(numbers[62:93]) < 2:
        return None
    first_smallest, second_smallest = (min(numbers[62:93]), min(numbers[62:93][1:]) + min(numbers[62:93]))
    for num in numbers[62:93]:
        if num == first_smallest:
            continue
        if num < second_smallest:
            second_smallest = num
    return None if second_smallest == first_smallest else second_smallest