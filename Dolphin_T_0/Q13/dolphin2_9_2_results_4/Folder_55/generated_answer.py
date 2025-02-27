def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    max_num = max(numbers[:11])
    sec_max_num = float('-inf')
    for num in numbers[:11]:
        if num > sec_max_num and num < max_num:
            sec_max_num = num
    if sec_max_num == float('-inf'):
        return None
    else:
        return sec_max_num