def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 200 or len(numbers) > 10000:
        return None
    min_num = float('inf')
    second_largest = float('-inf')
    for num in numbers[100:201]:
        if num < min_num:
            min_num = num
        elif num > min_num and num < second_largest:
            second_largest = num
    if second_largest == float('-inf'):
        return None
    else:
        return second_largest