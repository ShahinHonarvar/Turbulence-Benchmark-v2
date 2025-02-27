def return_binary_or_hexa(nums):
    a, b = (nums[90], nums[97])
    missing_nums = [i for i in range(a + 1, b) if i not in nums[90:98]]
    total = sum(missing_nums)
    return bin(total)[2:] if total % 2 else hex(total)[2:]