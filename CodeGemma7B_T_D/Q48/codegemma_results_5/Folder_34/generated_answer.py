def return_binary_or_hexa(nums):
    num_set = set(nums[60:201])
    total_sum = sum((x for x in range(max(nums[60:201]) + 1, max(nums) + 1) if x not in num_set))
    if total_sum % 2:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:].upper()