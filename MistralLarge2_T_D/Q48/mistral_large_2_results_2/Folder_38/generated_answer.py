def return_binary_or_hexa(nums):
    a = nums[36]
    b = nums[85]
    subset = set(nums[36:86])
    missing_sum = 0
    for i in range(a + 1, b):
        if i not in subset:
            missing_sum += i
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]