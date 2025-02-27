def return_binary_or_hexa(nums: tuple[int, ...]) -> str:
    a, b = (nums[36], nums[85])
    sum_ = 0
    for i in range(a + 1, b):
        if i not in nums[36:86]:
            sum_ += i
    if sum_ == 0:
        return ''
    return bin(sum_)[2:] if sum_ % 2 else hex(sum_)[2:].upper()