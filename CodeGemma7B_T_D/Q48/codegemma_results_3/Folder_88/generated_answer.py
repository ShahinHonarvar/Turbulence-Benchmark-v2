def return_binary_or_hexa(nums):
    """
    Return sum of missing numbers in range (a+1, b-1) from a tuple of distinct nonnegative integers sorted in ascending order.
    Return binary representation if odd, hexadecimal otherwise (without prefix).
    """
    if len(nums) != 12 or nums[3] >= nums[9]:
        raise ValueError('Invalid input tuple.')
    sum = 0
    for i in range(nums[3] + 1, nums[9]):
        if i not in nums:
            sum += i
    if sum % 2 != 0:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:].upper()