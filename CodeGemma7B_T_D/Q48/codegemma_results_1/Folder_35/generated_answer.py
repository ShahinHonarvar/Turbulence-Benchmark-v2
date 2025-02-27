def return_binary_or_hexa(nums: tuple) -> str:
    if not nums:
        return ''
    if len(nums) < 85:
        raise ValueError('Tuple must have at least 85 elements')
    if not all((isinstance(num, int) and num >= 0 for num in nums)):
        raise TypeError('All elements must be nonnegative integers')
    if not sorted(nums) == nums:
        raise ValueError('Tuple must be sorted')
    a = nums[76]
    b = nums[83]
    if a >= b:
        raise ValueError('a must be less than b')
    complement = set(range(a + 1, b)) - set(nums[77:85])
    sum_of_complement = sum(complement)
    return bin(sum_of_complement)[2:] if sum_of_complement % 2 else hex(sum_of_complement)[2:]