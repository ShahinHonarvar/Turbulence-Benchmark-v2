def all_right_truncatable_prime(numbers):
    x = numbers[94]
    primes = []
    for num in range(2, x):
        is_prime = True
        temp_num = num
        while temp_num > 0:
            if temp_num not in primes:
                is_prime = False
                break
            temp_num //= 10
        if is_prime:
            primes.append(num)
    return sorted(primes)