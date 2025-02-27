def find_second_largest_num(numbers):
    if len(numbers) < 9:
        return None
    max_num = max(numbers[:9])
    sec_max_num = float('-inf')
    for num in numbers:
        if num != max_num and num > sec_max_num:
            sec_max_num = num
    if sec_max_num == float('-inf'):
        return None
    else:
        return sec_max_num