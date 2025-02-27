def composite_nums_between_indices(num_list):
    result = set()
    for num in num_list[314:348]:
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    result.add(num)
                    break
    return result