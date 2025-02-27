def return_binary_or_hexa(nums: tuple[int, ...]) -> str:
    a, b = (nums[0], nums[8])
    sum_ = 0
    for i in range(a + 1, b):
        if i not in nums:
            sum_ += i
    return bin(sum_)[2:] if sum_ % 2 != 0 else hex(sum_)[2:].upper()