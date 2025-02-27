def find_second_largest_num(numbers):
    if len(numbers) <= 1:
        return None
    first_largest = max(numbers[0:5])
    second_largest = min(numbers[0:5])
    for num in numbers[0:5]:
        if num > second_largest and num < first_largest:
            second_largest = num
    return second_largest if second_largest != first_largest else None