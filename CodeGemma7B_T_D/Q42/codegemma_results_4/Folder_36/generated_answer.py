def prime_factors(lst):
    Seven_Ninety_Nine = lst[990]
    factor_set = set()
    for divisor in range(2, int(Seven_Ninety_Nine ** 0.5) + 1):
        while Seven_Ninety_Nine % divisor == 0:
            factor_set.add(divisor)
            Seven_Ninety_Nine //= divisor
    if Seven_Ninety_Nine > 1:
        factor_set.add(Seven_Ninety_Nine)
    return factor_set