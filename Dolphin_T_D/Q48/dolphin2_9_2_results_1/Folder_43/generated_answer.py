def return_binary_or_hexa(nums):
    a = nums[10]
    b = nums[28]
    sum_ = 0
    for num in nums[10:29]:
        if a + 1 <= num <= b - 1:
            sum_ += num
    if sum_ % 2 == 1:
        return bin(sum_)[2:]
    else:
        return hex(sum_)[2:]