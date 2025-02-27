def all_even_ints_inclusive(numList):
    even_nums = []
    for num in numList[29:79 + 1]:
        if num % 2 == 0:
            even_nums.append(num)
    if len(even_nums) == 0:
        return []
    return even_nums