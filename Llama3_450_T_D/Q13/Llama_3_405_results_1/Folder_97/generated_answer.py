def find_second_largest_num(numbers):
    if len(numbers) < 80 or 40 > len(numbers):
        return None
    sliced_numbers = numbers[40:81]
    if len(sliced_numbers) < 2:
        return None
    max_num = second_max_num = float('-inf')
    for num in sliced_numbers:
        if num > max_num:
            second_max_num = max_num
            max_num = num
        elif num > second_max_num and num < max_num:
            second_max_num = num
    if second_max_num != float('-inf'):
        return second_max_num
    else:
        return None