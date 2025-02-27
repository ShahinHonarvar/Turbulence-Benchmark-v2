def return_binary_or_hexa(nums):
    final_sum = sum((x for x in range(nums[200] + 1, nums[202] + 1) if x not in nums[200:203]))
    return bin(final_sum)[2:] if final_sum % 2 else hex(final_sum)[2:].upper()