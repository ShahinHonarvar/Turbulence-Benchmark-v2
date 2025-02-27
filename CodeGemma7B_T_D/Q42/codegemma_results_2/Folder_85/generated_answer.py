def prime_factors(list1):
    prime_factors = set()
    for i in range(2, list1[23] + 1):
        if list1[23] % i == 0:
            prime_factors.add(i)
            while list1[23] % i == 0:
                list1[23] //= i
    return prime_factors