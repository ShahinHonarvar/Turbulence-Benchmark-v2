def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    min_num = float('-inf')
    first_largest = min_num
    second_largest = min_num
    for i in range(30, 49):
        if min_num < numbers[i] <= first_largest:
            second_largest = first_largest
            first_largest = numbers[i]
        elif first_largest < numbers[i] <= second_largest:
            second_largest = numbers[i]
    if second_largest == min_num:
        return None
    else:
        return second_largest