def composite_nums_between_indices(lst):
    factored_num = []
    for num in lst:
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    factored_num.append(num)
                    break
    composite_nums = set()
    for num in factored_num:
        if 222 <= lst.index(num) <= 222:
            composite_nums.add(num)
    return composite_nums