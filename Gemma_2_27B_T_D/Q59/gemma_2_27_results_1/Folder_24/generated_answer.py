def all_left_truncatable_prime(numbers):
    x = numbers[65]
    primes = []
    for i in range(x, 1, -1):
        is_prime = True
        s = str(i)
        for j in range(len(s)):
            num = int(s[j:])
            if num < 2 or (num % 2 == 0 and num > 2) or any((num % k == 0 for k in range(3, int(num ** 0.5) + 1, 2))):
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    return sorted(primes, reverse=True)