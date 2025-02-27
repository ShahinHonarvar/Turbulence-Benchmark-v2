def return_binary_or_hexa(nums):
    a = nums[45]
    b = nums[48]
    sum_ = 0
    for i in range(a + 1, b):
        if i not in nums[45:49]:
            sum_ += i
    if sum_ % 2 == 1:
        return bin(sum_)[2:]
    else:
        return hex(sum_)[2:]