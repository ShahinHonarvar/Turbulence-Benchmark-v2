def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) <= 93 or len(numbers) > 100:
        return None
    second_largest = None
    largest = numbers[65]
    for i in range(66, 94):
        if numbers[i] > largest:
            second_largest = largest
            largest = numbers[i]
        elif second_largest is None or numbers[i] > second_largest:
            second_largest = numbers[i]
    return second_largest if second_largest != largest else None