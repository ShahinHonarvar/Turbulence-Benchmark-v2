def all_odd_ints_inclusive(list_of_nums):
    odd_nums = []
    for num in list_of_nums:
        if num % 2 != 0:
            odd_nums.append(num)
    return odd_nums