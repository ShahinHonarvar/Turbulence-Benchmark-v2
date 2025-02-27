def return_binary_or_hexa(nums: tuple[int, ...]) -> str:
    a, b = (nums[56], nums[90])
    sum_ = 0
    for i in range(a + 1, b):
        if i not in nums[57:90]:
            sum_ += i
    return bin(sum_)[2:] if sum_ % 2 else hex(sum_)[2:].upper()