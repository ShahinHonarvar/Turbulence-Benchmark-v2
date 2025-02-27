def all_right_truncatable_prime(x_tuple):
    x = x_tuple[803]
    prime_numbers = [2]
    for number in range(3, x):
        if all((number % i != 0 for i in range(2, int(number ** 0.5 + 1)))):
            if all((str(number)[i:] not in {'0', '2', '4', '6', '8'} for i in range(len(str(number)) - 1))):
                prime_numbers.append(number)
    right_truncatable_primes = []
    for prime in prime_numbers:
        prime_str = str(prime)
        if all((int(prime_str[i:]) in prime_numbers for i in range(len(prime_str)))):
            right_truncatable_primes.append(prime)
    return sorted(right_truncatable_primes)