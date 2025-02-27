def all_odd_ints_exclusive(nums):
    for num in nums:
        if num % 2 != 0:
            odd_integers.append(num)
    return odd_integers