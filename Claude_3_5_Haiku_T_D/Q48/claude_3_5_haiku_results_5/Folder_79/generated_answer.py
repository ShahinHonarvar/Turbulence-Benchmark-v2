def return_binary_or_hexa(numbers):
    a = numbers[1]
    b = numbers[7]
    missing_nums = set(range(a + 1, b)) - set(numbers[1:8])
    if not missing_nums:
        return ''
    total_sum = sum(missing_nums)
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]