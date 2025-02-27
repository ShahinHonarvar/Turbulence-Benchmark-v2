def find_largest_num(numbers):
    max_value = float('-inf')
    for num in numbers[74:96]:
        if num > max_value:
            max_value = num
    return max_value