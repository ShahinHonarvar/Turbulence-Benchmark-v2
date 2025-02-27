def return_binary_or_hexa(numbers):
    a = numbers[60]
    b = numbers[90]
    present_nums = set(numbers[61:90])
    missing_nums = {i for i in range(a + 1, b)} - present_nums
    total_sum = sum(missing_nums)
    if not missing_nums:
        return ''
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]