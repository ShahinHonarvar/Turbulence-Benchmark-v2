def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 13 or len(numbers) < 68:
        return None
    first, second = (max(numbers[13:68]), None)
    for num in numbers[13:68]:
        if num < first:
            second = num
            break
    for num in numbers[13:68]:
        if num > second and num < first:
            second = num
    if second is not None and second != first:
        return second
    else:
        return None