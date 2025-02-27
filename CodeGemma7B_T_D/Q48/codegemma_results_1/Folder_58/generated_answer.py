def return_binary_or_hexa(nums):
    a = nums[275]
    b = nums[871]
    sum_ = sum(range(a + 1, b))
    present = {n for n in nums[275:872]}
    missing = sum_ - sum(present)
    return format(missing, 'b') if missing % 2 else format(missing, 'x')