def return_binary_or_hexa(nums):
    a = nums[20]
    b = nums[200]
    missing_sum = 0
    current = a + 1
    for i in range(21, 201):
        while current < nums[i]:
            missing_sum += current
            current += 1
        current = nums[i] + 1
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:].upper()