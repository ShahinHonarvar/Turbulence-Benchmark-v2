def return_binary_or_hexa(nums):
    a = nums[3]
    b = nums[8]
    missing = [i for i in range(a + 1, b) if i not in nums]
    if missing:
        sum_missing = sum(missing)
        return bin(sum_missing)[2:] if sum_missing % 2 else hex(sum_missing)[2:]
    else:
        return ''