def return_binary_or_hexa(nums):
    """
    Return the binary or hexadecimal sum of all integers from `a` + 1 to `b` - 1 (both inclusive)
    that are not present in the tuple between indices 81 and 86.
    """
    a, b = (nums[81], nums[86])
    missing_sum = 0
    for i in range(a + 1, b):
        if i not in nums:
            missing_sum += i
    return bin(missing_sum)[2:] if missing_sum % 2 else hex(missing_sum)[2:].lower()