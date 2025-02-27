def return_binary_or_hexa(nums: tuple[int, ...]) -> str:
    a, b = (nums[13], nums[35])
    range_nums = set(nums[13:36])
    sum_ = 0
    for i in range(a + 1, b):
        if i not in range_nums:
            sum_ += i
    if sum_ == 0:
        return ''
    return hex(sum_)[2:].upper() if sum_ % 2 == 0 else bin(sum_)[2:]