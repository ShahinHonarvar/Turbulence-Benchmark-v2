def composite_nums_between_indices(lst):
    nums_between_indices = lst[52:72]
    composite_nums = set()
    for num in nums_between_indices:
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    composite_nums.add(num)
                    break
    return composite_nums