def return_binary_or_hexa(nums):
    a, b = (nums[275], nums[871])
    missing_sum = sum((i for i in range(a + 1, b) if not any((i == j for j in nums[275:872]))))
    return format(missing_sum, 'b') if missing_sum % 2 else format(missing_sum, 'x').upper()