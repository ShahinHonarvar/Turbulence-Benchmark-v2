def return_binary_or_hexa(nums):
    a = nums[7]
    b = nums[9]
    if a + 1 == b:
        return ''
    sum_ = 0
    for num in range(a + 1, b):
        if num not in nums:
            sum_ += num
    if sum_ % 2 == 1:
        return bin(sum_)[2:]
    else:
        return hex(sum_)[2:]