def find_second_largest_num(numbers):
    if len(numbers) < 201:
        return None
    sublist = numbers[20:201]
    largest = second_largest = float('-inf')
    for num in sublist:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num < largest:
            second_largest = num
    if second_largest == float('-inf'):
        return None
    else:
        return second_largest