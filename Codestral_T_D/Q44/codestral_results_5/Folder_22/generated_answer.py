def composite_nums_between_indices(num_list):
    composite_nums = set()
    for i in range(50, 201):
        num = num_list[i]
        divisors = set()
        for j in range(2, int(num ** 0.5) + 1):
            if num % j == 0:
                divisors.add(j)
                divisors.add(num // j)
            if len(divisors) > 1:
                composite_nums.add(num)
                break
    return composite_nums