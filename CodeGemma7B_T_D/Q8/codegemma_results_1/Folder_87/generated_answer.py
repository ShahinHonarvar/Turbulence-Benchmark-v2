def all_even_ints_exclusive(nums):
    lst = []
    for num in nums[32:99]:
        if num % 2 == 0:
            lst.append(num)
    return lst