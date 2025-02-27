def return_binary_or_hexa(tup):
    a, _, _, b = tup
    missing_nums = [i for i in range(a + 1, b) if i not in tup]
    nums_sum = sum(missing_nums)
    if nums_sum == 0:
        return ''
    return bin(nums_sum)[2:] if nums_sum % 2 != 0 else hex(nums_sum)[2:]