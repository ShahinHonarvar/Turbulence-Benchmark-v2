def find_second_largest_num(numbers):
    second_largest = None
    largest = float('-inf')
    for num in numbers[15:52]:
        if num > largest:
            second_largest = largest
            largest = num
        elif num < largest and num > second_largest:
            second_largest = num
    return second_largest