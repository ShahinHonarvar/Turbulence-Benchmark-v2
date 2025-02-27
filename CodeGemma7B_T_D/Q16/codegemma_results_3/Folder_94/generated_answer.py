def sum_even_ints_inclusive(nums):
    if not isinstance(nums, list) or not all((isinstance(num, int) for num in nums)):
        raise TypeError('Invalid input arguments. Expected a list of integers.')
    even_ints = []
    for i in range(28, 41):
        if i in range(len(nums)) and nums[i] % 2 == 0:
            even_ints.append(nums[i])
    return sum(even_ints) if even_ints else 0