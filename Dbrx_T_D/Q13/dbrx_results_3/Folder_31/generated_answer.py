def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) <= 89 - 75:
        return None
    second_largest = None
    largest = float('-inf')
    for num in numbers[75:89]:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num < largest:
            second_largest = num
    if second_largest == None:
        for num in numbers:
            if num > largest:
                second_largest = largest
                largest = num
            elif num > second_largest and num < largest:
                second_largest = num
    return second_largest