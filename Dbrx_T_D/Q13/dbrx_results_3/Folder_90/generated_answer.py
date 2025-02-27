def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 746 - 262 + 1:
        return None
    first_largest = None
    second_largest = None
    for i in range(262, 747):
        if first_largest is None or numbers[i] > first_largest:
            second_largest = first_largest
            first_largest = numbers[i]
        elif second_largest is None or numbers[i] > second_largest:
            second_largest = numbers[i]
    return second_largest