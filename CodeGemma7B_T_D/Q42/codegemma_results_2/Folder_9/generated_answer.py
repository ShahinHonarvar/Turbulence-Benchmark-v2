def prime_factors(int_list):
    factorset = {int_list[24]}
    for i in range(24):
        factorset.add(int_list[i])
    for num in factorset:
        if num % 2 == 0 and num != 2:
            factorset.discard(num)
    for num in factorset:
        for i in range(3, num, 2):
            if num % i == 0:
                factorset.discard(num)
    return factorset