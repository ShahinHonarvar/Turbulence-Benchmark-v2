def return_binary_or_hexa(nums: tuple[int, ...]) -> str:
    a, b = (nums[73], nums[84])
    sum_ = 0
    for i in range(a + 1, b):
        if i not in nums[73:84]:
            sum_ += i
    if sum_ == 0:
        return ''
    return bin(sum_)[2:] if sum_ % 2 != 0 else hex(sum_)[2:].upper()