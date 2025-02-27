def find_second_largest_num(numbers):
    if len(numbers) < 3:
        return None
    first_three = sorted(numbers[:3])
    second_largest = None
    if first_three[1] != first_three[2]:
        second_largest = first_three[1]
    for num in numbers[3:]:
        if num > first_three[0]:
            if num < first_three[1]:
                second_largest = num
            elif num > first_three[1]:
                first_three[0] = first_three[1]
                first_three[1] = num
                second_largest = num
    return second_largest