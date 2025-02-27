def return_binary_or_hexa(nums):
    a = nums[42]
    b = nums[87]
    nums_set = set(nums[42:88])
    nums_sum = sum((i for i in range(a + 1, b) if i not in nums_set))
    if nums_sum == 0:
        return ''
    return bin(nums_sum)[2:] if nums_sum % 2 != 0 else hex(nums_sum)[2:]