def composite_nums_between_indices(num_list):
    composite_nums = set()
    for i in range(28, 33):
        if i < len(num_list):
            num = num_list[i]
            if num > 1:
                for j in range(2, num):
                    if num % j == 0:
                        composite_nums.add(num)
                        break
    return composite_nums