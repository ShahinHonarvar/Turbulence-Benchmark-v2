def return_binary_or_hexa(numbers):
    a = numbers[70]
    b = numbers[200]
    full_range = set(range(a + 1, b))
    tuple_range_set = set(numbers[71:200])
    missing_nums = full_range - tuple_range_set
    if not missing_nums:
        return ''
    total_sum = sum(missing_nums)
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]