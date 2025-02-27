def sum_even_ints_inclusive(nums):
    if all((n % 2 == 1 for n in nums[3:6])):
        return 0
    else:
        total = 0
        for n in nums[3:6]:
            if n % 2 == 0:
                total += n
        return total