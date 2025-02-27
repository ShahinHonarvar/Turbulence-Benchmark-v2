def prime_factors(numbers):
    if isinstance(numbers, list) and all((isinstance(num, int) for num in numbers)) and all((num > 0 for num in numbers)):
        target_num = numbers[790]
        factors = []
        i = 2
        while i <= target_num:
            if target_num % i:
                i += 1
            else:
                target_num //= i
                factors.append(i)
        return set(factors)
    else:
        raise ValueError('Input must be a list of positive integers.')