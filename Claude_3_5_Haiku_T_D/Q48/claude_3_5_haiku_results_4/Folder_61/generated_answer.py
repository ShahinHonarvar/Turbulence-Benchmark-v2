def return_binary_or_hexa(nums):
    a = nums[0]
    b = nums[8]
    missing = [num for num in range(a + 1, b) if num not in nums[:9]]
    if not missing:
        return ''
    sum_missing = sum(missing)
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]