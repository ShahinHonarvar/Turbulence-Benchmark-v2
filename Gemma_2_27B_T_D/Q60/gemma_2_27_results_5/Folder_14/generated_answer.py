def all_left_right_truncatable_prime(numbers):
    x = numbers[78]
    primes = []
    for i in range(2, x + 1):
        s = str(i)
        if '0' not in s:
            is_prime = True
            while len(s) > 1:
                if not (int(s) and all((int(s) % j for j in range(2, int(s ** 0.5) + 1)))):
                    is_prime = False
                    break
                s = s[1:-1]
            if is_prime and (int(s) and all((int(s) % j for j in range(2, int(s ** 0.5) + 1)))):
                primes.append(i)
    return sorted(primes, reverse=True)