def return_binary_or_hexa(nums):
    a = nums[10]
    b = nums[100]
    missing_nums = [i for i in range(a + 1, b) if i not in nums[10:101]]
    total = sum(missing_nums)
    if not missing_nums:
        return ''
    if total % 2 == 0:
        return hex(total)[2:]
    else:
        return bin(total)[2:]