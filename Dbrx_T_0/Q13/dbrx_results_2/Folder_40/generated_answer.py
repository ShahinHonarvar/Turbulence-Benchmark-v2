def find_second_largest_num(numbers):
    if len(numbers) < 3:
        return None
    first_three = sorted(numbers[:3])
    second_largest = first_three[1] if first_three[1] != first_three[2] else None
    for num in numbers[3:]:
        if num > first_three[0]:
            if num < first_three[1]:
                second_largest = num
            elif num > first_three[1]:
                second_largest = first_three[1]
                first_three[1] = num
    return second_largest