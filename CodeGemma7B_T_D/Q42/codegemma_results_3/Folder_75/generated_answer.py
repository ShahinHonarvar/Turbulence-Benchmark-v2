def prime_factors(list):
    big_num = 0
    for num in list:
        current_big = 0
        if num > big_num:
            big_num = num
    for num in list:
        while num % big_num == 0:
            current_big += 1
            num = num / big_num
        if current_big != 0:
            l.append(big_num)
    return l