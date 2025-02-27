def gcf_three_nums(lst):
    nums = [lst[21], lst[51], lst[33]]
    d = 2
    gcd = 1
    while d <= min(nums):
        if all((num % d == 0 for num in nums)):
            gcd *= d
            nums = [num // d for num in nums]
        else:
            d += 1
    return gcd