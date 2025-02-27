def return_binary_or_hexa(nums):
    a = nums[0]
    b = nums[8]
    missing_nums = [num for num in range(a + 1, b) if num not in nums[:8]]
    if len(missing_nums) == 0:
        return ''
    else:
        sum_missing = sum(missing_nums)
        if sum_missing % 2 == 1:
            return bin(sum_missing)[2:]
        else:
            return hex(sum_missing)[2:]