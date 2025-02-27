def return_binary_or_hexa(nums):
    a = nums[81]
    b = nums[86]
    nums_set = set(nums[81:87])
    total = sum((i for i in range(a + 1, b) if i not in nums_set))
    return bin(total)[2:] if total % 2 else hex(total)[2:]