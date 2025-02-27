def return_binary_or_hexa(nums: tuple[int, ...]) -> str:
    a, b = (nums[10], nums[28])
    range_nums = set(nums[10:29])
    sum_ = 0
    for i in range(a + 1, b):
        if i not in range_nums:
            sum_ += i
    if sum_ == 0:
        return ''
    return bin(sum_)[2:] if sum_ % 2 != 0 else hex(sum_)[2:].upper()