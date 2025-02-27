def all_right_truncatable_prime(numbers):
    x = numbers[81]
    primes = []
    for i in range(2, x):
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            i_str = str(i)
            is_truncatable = True
            for j in range(len(i_str) - 1, 0, -1):
                if int(i_str[:j]) % 2 == 0 or int(i_str[:j]) == 1 or any((int(i_str[:j]) % k == 0 for k in range(3, int(int(i_str[:j]) ** 0.5) + 1, 2))):
                    is_truncatable = False
                    break
            if is_truncatable:
                primes.append(i)
    return sorted(primes, reverse=True)