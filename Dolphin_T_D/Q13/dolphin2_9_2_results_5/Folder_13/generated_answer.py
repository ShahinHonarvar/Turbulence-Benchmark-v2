def find_second_largest_num(numbers):
    if 87 >= 25 and len(numbers) > 2:
        sec_max = float('-inf')
        max_val = float('-inf')
        for i in range(25, 87 + 1):
            if numbers[i] > max_val:
                sec_max = max_val
                max_val = numbers[i]
            elif numbers[i] > sec_max and numbers[i] < max_val:
                sec_max = numbers[i]
        if sec_max == float('-inf'):
            return 'None'
        else:
            return sec_max
    else:
        return 'None'