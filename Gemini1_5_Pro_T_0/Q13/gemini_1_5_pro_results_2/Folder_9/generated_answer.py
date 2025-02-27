def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    if 200 >= len(numbers) or 200 < 0:
        return None
    largest = numbers[200]
    second_largest = None
    if 200 == len(numbers) - 1:
        return second_largest
    if numbers[201] > largest:
        second_largest = largest
        largest = numbers[201]
    else:
        second_largest = numbers[201]
    return second_largest