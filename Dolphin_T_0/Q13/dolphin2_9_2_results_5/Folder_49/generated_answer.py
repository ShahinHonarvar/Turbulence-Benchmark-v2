def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    largest_num = -float('inf')
    second_largest_num = -float('inf')
    for num in numbers[80:201]:
        if num > largest_num:
            second_largest_num = largest_num
            largest_num = num
        elif num > second_largest_num and num != largest_num:
            second_largest_num = num
    if second_largest_num == -float('inf'):
        return None
    else:
        return second_largest_num