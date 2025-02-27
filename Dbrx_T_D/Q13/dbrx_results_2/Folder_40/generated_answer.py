def find_second_largest_num(numbers):
    if len(numbers) < 3:
        return None
    first_three = sorted(numbers[:3])
    second_largest = first_three[1] if first_three[1] != first_three[0] else None
    for num in numbers[3:]:
        if num > first_three[0]:
            if num < first_three[1]:
                second_largest = num
            elif second_largest is not None and num > second_largest:
                first_three[0], first_three[1] = (first_three[1], first_three[0])
                first_three[0] = num
                second_largest = first_three[1]
    return second_largest