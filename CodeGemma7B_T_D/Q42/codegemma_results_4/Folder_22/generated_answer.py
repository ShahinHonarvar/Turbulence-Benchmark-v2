def prime_factors(lst):
    prime_factors = set()
    for num in lst:
        if type(num) != int:
            raise TypeError('list should contain only positive integers')
        if num <= 0:
            raise ValueError('list should contain only positive integers')
    number = lst[72]
    for factor in range(2, number + 1):
        while number % factor == 0:
            prime_factors.add(factor)
            number //= factor
    return prime_factors