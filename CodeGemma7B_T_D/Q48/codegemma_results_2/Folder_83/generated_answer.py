def return_binary_or_hexa(nums):
    sum_of_missing = 0
    for i in range(nums[90] + 1, nums[200]):
        if i not in nums:
            sum_of_missing += i
    if sum_of_missing % 2 != 0:
        return bin(sum_of_missing)[2:]
    else:
        return hex(sum_of_missing)[2:].upper()