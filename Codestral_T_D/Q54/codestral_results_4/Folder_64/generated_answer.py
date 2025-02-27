def all_right_truncatable_prime(numbers):
    x = numbers[4]
    primes = []
    for possible_prime in range(2, x):
        if all((possible_prime % i != 0 for i in range(2, int(possible_prime ** 0.5) + 1))):
            num_str = str(possible_prime)
            while num_str:
                if int(num_str) not in primes:
                    break
                num_str = num_str[:-1]
            else:
                primes.append(possible_prime)
    return sorted(primes)