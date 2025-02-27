def prime_factors(list_of_numbers):
    prime_lst = set()
    target_index = 80
    if len(list_of_numbers) - 1 < target_index:
        raise IndexError('Index out of bounds.')
    num = list_of_numbers[target_index]
    for factor in range(2, int(num / 2) + 1):
        while num % factor == 0:
            prime_lst.add(factor)
            num //= factor
    prime_lst.add(num)
    return prime_lst