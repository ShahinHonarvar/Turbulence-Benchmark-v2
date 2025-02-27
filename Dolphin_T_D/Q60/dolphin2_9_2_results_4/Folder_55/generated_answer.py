def all_left_right_truncatable_prime(numbers_tuple):
    x = numbers_tuple[73]
    primes = []
    for num in range(x, 0, -1):
        if all((num % i != 0 for i in range(2, num))):
            num_str = str(num)
            if '0' not in num_str:
                while len(num_str) > 1:
                    if all((int(num_str[i:]) % j != 0 for i in range(1, len(num_str)) for j in range(2, int(num_str[i:])))):
                        num_str = num_str[1:-1]
                    else:
                        break
                if len(num_str) <= 1 and num not in primes:
                    primes.append(num)
    return sorted(primes, reverse=True)