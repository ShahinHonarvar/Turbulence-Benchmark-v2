def find_smallest_num(numbers):
    min_num = float('inf')
    for num in numbers[74:96]:
        if num < min_num:
            min_num = num
    return min_num