def prime_factors(lst):
    num = lst[23]
    result = set()
    while num % 2 == 0:
        num //= 2
        result.add(2)
    for i in range(3, int(num ** 0.5) + 1, 2):
        while num % i == 0:
            num //= i
            result.add(i)
    if num != 1:
        result.add(num)
    return result