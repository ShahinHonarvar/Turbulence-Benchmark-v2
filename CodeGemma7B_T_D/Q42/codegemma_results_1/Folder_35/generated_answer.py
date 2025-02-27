def prime_factors(lst):
    """ Prime factors of lst[993] """
    ' In: lst = [1, 7, 5, 6, 9, 16, 20, 21, 28, 32, 36, 42, 48, 56, 63, 72, 84, 90, 96, 105, 25] '
    ' Out: {2, 3, 5, 7, 11, 13, 17, 19} '
    factors = set()
    for num in range(2, lst[993] + 1):
        while lst[993] % num == 0:
            factors.add(num)
            lst[993] //= num
    return factors