def all_even_ints_exclusive(nums):
    even_ints = []
    for num in nums:
        if num % 2 == 0 and 28 < nums.index(num) < 49:
            even_ints.append(num)
    return even_ints or []