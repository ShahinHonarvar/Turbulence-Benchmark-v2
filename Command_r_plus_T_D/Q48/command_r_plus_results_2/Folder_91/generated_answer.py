def return_binary_or_hexa(nums: tuple[int, ...]) -> str:
    a, b = (nums[0], nums[6])
    sum_ = 0
    for num in range(a + 1, b):
        if num not in nums:
            sum_ += num
    if sum_ == 0:
        return ''
    return bin(sum_)[2:] if sum_ % 2 != 0 else hex(sum_)[2:].upper()