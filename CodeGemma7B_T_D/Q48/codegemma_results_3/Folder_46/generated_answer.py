def return_binary_or_hexa(nums):
    nums = nums[10:79]
    nums.sort()
    sum_nums = 0
    for num in range(nums[0] + 1, nums[-1]):
        if num not in nums:
            sum_nums += num
    if sum_nums % 2:
        return bin(sum_nums)[2:]
    else:
        return hex(sum_nums)[2:].upper()