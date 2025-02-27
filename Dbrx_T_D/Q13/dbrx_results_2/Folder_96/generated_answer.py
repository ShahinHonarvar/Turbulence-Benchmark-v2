def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 38:
        return None
    sorted_numbers = sorted(numbers[14:52])
    if len(set(sorted_numbers)) < 2:
        return None
    second_largest = None
    for num in sorted_numbers[::-1]:
        if num < sorted_numbers[-1]:
            second_largest = num
            break
    return second_largest