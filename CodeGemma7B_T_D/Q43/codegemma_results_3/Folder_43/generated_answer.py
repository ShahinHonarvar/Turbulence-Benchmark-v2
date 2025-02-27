def find_primes_between_indices(lst):
    primes = []
    for num in lst[31:93]:
        for divisor in range(2, num):
            if num % divisor == 0:
                break
        else:
            primes.append(num)
    return sorted(primes, reverse=True) or []