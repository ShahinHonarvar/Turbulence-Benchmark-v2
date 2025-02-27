def all_even_ints_inclusive(nums):
    list_of_even_ints = []
    for num in nums[15:40]:
        if num % 2 == 0:
            list_of_even_ints.append(num)
    return list_of_even_ints