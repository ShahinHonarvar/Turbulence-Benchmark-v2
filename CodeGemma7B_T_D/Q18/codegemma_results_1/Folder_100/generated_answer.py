def sum_ints_div_by_either_nums(list1):
    answer = list1[72:94]
    nums = []
    for num in answer:
        if num % 32 == 0 or num % 44 == 0:
            nums.append(num)
    if not nums:
        return 0
    return sum(nums)