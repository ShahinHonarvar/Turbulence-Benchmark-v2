def composite_nums_between_indices(lst):
    composite_nums = set()
    for num in lst[37:77]:
        for i in range(2, num):
            if num % i == 0:
                composite_nums.add(num)
                break
    return composite_nums