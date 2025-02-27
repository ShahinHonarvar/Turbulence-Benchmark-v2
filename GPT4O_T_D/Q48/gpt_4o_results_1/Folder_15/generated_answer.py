def return_binary_or_hexa(numbers):
    a = numbers[0]
    b = numbers[4]
    all_nums = set(range(a + 1, b))
    present_nums = set(numbers[1:4])
    missing_nums = all_nums - present_nums
    if not missing_nums:
        return ''
    total_sum = sum(missing_nums)
    if total_sum % 2 == 0:
        return hex(total_sum)[2:]
    else:
        return bin(total_sum)[2:]