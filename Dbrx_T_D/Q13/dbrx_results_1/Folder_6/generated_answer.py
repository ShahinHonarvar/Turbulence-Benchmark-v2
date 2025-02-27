def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 67 or len(numbers) - 66 != 10:
        return None
    start, end = (numbers[10], numbers[11:66])
    second_largest, largest = (None, start)
    for num in end:
        if num > largest:
            second_largest = largest
            largest = num
        elif second_largest is None or num > second_largest:
            second_largest = num
    return second_largest if second_largest < largest else None