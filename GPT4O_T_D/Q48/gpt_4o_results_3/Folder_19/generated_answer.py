def return_binary_or_hexa(numbers):
    a = numbers[1]
    b = numbers[4]
    nums_between = set(numbers[1:5])
    required_nums = set(range(a + 1, b))
    missing_nums = required_nums - nums_between
    if not missing_nums:
        return ''
    total_sum = sum(missing_nums)
    if total_sum % 2:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]