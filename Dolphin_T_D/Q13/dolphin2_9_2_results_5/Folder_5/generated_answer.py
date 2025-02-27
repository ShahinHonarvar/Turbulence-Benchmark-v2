def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    numbers = numbers[7:10]
    max_num = max(numbers)
    sec_max_num = float('-inf')
    for num in numbers:
        if num != max_num and num > sec_max_num:
            sec_max_num = num
    return sec_max_num if sec_max_num != float('-inf') else None