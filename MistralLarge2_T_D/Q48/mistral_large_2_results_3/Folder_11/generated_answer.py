def return_binary_or_hexa(nums):
    a, b = (nums[48], nums[76])
    present = set(nums[48:77])
    total_sum = sum((num for num in range(a + 1, b) if num not in present))
    if total_sum == 0:
        return ''
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]