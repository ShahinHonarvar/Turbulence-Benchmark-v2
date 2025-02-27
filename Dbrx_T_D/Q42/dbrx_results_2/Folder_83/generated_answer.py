def prime_factors(numbers_list):
    if len(numbers_list) <= 95:
        return 'The list should have at least 96 elements.'
    else:
        num = numbers_list[95]
        i = 2
        factors = []
        while i * i <= num:
            if num % i:
                i += 1
            else:
                num //= i
                factors.append(i)
        if num > 1:
            factors.append(num)
        return set(factors)