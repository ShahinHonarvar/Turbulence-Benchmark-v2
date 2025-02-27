def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 98:
        return None
    second_largest = None
    largest = max(numbers[21:98])
    for num in numbers[21:98]:
        if num > second_largest and num < largest:
            second_largest = num
    if second_largest == largest:
        return None
    else:
        return second_largest