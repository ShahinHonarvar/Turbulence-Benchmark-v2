def return_binary_or_hexa(nums):
    a = nums[16]
    b = nums[87]
    if a + 1 == b:
        return ''
    missing_nums = [num for num in range(a + 1, b) if num not in nums[16:88]]
    if not missing_nums:
        return ''
    total = sum(missing_nums)
    if total % 2 == 0:
        return hex(total)[2:]
    else:
        return bin(total)[2:]