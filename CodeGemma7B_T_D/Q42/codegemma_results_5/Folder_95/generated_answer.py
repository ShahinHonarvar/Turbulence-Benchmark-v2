def prime_factors(a):
    result = set()
    target_number = a[87]
    for divisor in range(2, int(target_number ** 0.5) + 1):
        if target_number % divisor == 0:
            result.add(divisor)
            while target_number % divisor == 0:
                target_number //= divisor
    result.add(target_number)
    return result