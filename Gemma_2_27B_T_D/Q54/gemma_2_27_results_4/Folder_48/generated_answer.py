def all_right_truncatable_prime(numbers):
    x = numbers[835]
    primes = []
    for i in range(2, x):
        str_i = str(i)
        is_prime = True
        for j in range(len(str_i)):
            if not is_prime():
                break
            num = int(str_i[:len(str_i) - j])
            for k in range(2, int(num ** 0.5) + 1):
                if num % k == 0:
                    is_prime = False
                    break
        if is_prime:
            primes.append(i)
    return sorted(primes)