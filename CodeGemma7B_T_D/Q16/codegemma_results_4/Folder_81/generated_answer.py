def sum_even_ints_inclusive(lst):
    even_nums = []
    for num in lst[10:101]:
        if num % 2 == 0:
            even_nums.append(num)
    if not even_nums:
        return 0
    return sum(even_nums)