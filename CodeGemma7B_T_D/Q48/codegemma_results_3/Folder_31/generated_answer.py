def return_binary_or_hexa(nums):
    """
    Returns the binary or hexadecimal representation of the sum of all integers from a + 1 to b - 1 (both inclusive) that are not present in the tuple.
    """
    nums_set = set(nums)
    a, b = (nums[33], nums[78])
    sum_of_missing_nums = 0
    for i in range(a + 1, b):
        if i not in nums_set:
            sum_of_missing_nums += i
    if sum_of_missing_nums % 2 == 1:
        return bin(sum_of_missing_nums)[2:]
    else:
        return hex(sum_of_missing_nums)[2:].upper()