def all_even_ints_inclusive(nums):
    even_ints = []
    for i in range(527, 539):
        if nums[i] % 2 == 0 and i in range(527, 539):
            even_ints.append(nums[i])
    if even_ints == []:
        even_ints.append('no even integers')
    return even_ints