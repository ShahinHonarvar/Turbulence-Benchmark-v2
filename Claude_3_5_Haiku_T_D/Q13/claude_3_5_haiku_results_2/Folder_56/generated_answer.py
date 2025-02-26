def find_second_largest_num(numbers):
    if len(numbers) <= 1:
        return None
    largest = max(numbers[0])
    second_largest = None
    for num in numbers[0:1]:
        if num > largest:
            second_largest = largest
            largest = num
        elif num < largest and (second_largest is None or num > second_largest):
            second_largest = num
    return second_largest