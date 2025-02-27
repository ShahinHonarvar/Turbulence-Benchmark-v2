def composite_nums_between_indices(num_list):
    composite_nums = set()
    for num in num_list[3:6]:
        if num % 2 != 0:
            for factor in range(3, int(num ** 0.5) + 1):
                if num % factor == 0:
                    composite_nums.add(num)
                    break
    return composite_nums