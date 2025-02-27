def prime_factors(my_list):
    factor_set = set()
    while my_list[99] > 1:
        for num in range(2, my_list[99] + 1):
            if my_list[99] % num == 0:
                factor_set.add(num)
                my_list[99] //= num
        return factor_set