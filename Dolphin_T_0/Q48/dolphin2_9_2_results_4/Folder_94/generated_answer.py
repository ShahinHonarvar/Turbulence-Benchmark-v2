def return_binary_or_hexa(nums):
    a, b = (nums[42], nums[87])
    sum_ = 0
    for num in range(a + 1, b):
        if num not in nums:
            sum_ += num
    if sum_ % 2 == 1:
        return '{0:b}'.format(sum_)
    else:
        return '{:x}'.format(sum_)