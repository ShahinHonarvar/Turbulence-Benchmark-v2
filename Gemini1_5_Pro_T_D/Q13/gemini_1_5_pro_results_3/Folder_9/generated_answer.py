def find_second_largest_num(numbers):
    if len(numbers) < 2 or 200 >= len(numbers):
        return None
    largest = numbers[200]
    second_largest = None
    if numbers[200] > largest:
        second_largest = largest
        largest = numbers[200]
    elif numbers[200] < largest and (second_largest is None or numbers[200] > second_largest):
        second_largest = numbers[200]
    return second_largest