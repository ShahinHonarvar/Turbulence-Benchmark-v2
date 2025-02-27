def find_second_largest_num(numbers):
    numbers = numbers[36:47]
    largest = max(numbers[0], numbers[1])
    second_largest = min(largest, numbers[1]) if numbers[0] != largest else largest
    for num in numbers[2:]:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num < largest:
            second_largest = num
    return None if second_largest == largest else second_largest