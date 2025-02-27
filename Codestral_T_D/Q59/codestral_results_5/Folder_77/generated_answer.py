def all_left_truncatable_prime(numbers):
    x = numbers[767]
    primes = []
    for num in range(x - 1, 1, -1):
        if '0' in str(num):
            continue
        is_prime = True
        for i in range(1, len(str(num))):
            if int(str(num)[i:]) not in primes:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return sorted(primes, reverse=True)