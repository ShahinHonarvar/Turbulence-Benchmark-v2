def return_binary_or_hexa(nums):
    filtered_nums = [x for x in range(nums[50] + 1, nums[200]) if x not in nums]
    filtered_sum = sum(filtered_nums)
    if filtered_sum % 2 == 0:
        return hex(filtered_sum).replace('0x', '').lower()
    else:
        return bin(filtered_sum).replace('0b', '')