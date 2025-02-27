def return_binary_or_hexa(nums):
    missing_sum = sum(set(range(nums[0] + 1, nums[5] - 1)) - set(nums))
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum).split('x')[-1].upper()