def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 88:
        return None
    first_part = numbers[30:88]
    sorted_part = sorted(first_part)
    if len(sorted_part) < 2:
        return None
    second_largest = None
    for num in sorted_part[::-1]:
        if num < sorted_part[-1]:
            second_largest = num
            break
    return second_largest