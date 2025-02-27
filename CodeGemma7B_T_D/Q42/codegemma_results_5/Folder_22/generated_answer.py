def prime_factors(lst):
    prime_set = set()
    for idx in range(len(lst)):
        num = lst[idx]
        for divisor in range(2, int(num ** 0.5) + 1):
            if num % divisor == 0:
                prime_set.add(divisor)
                num = num // divisor
        if num > 1:
            prime_set.add(num)
    if len(prime_set) != 0:
        return prime_set[72]
    else:
        return -1