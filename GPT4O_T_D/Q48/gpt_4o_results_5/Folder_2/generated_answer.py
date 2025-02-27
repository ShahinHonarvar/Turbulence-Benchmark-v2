def return_binary_or_hexa(numbers):
    a = numbers[72]
    b = numbers[93]
    if b - a <= 1:
        return ''
    required_nums = set(range(a + 1, b))
    existing_nums = set(numbers[73:93])
    missing_nums = required_nums - existing_nums
    if not missing_nums:
        return ''
    total = sum(missing_nums)
    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]