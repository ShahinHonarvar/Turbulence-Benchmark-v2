def all_right_truncatable_prime(numbers):
    x = numbers[1]
    primes = []
    for num in range(2, x):
        is_prime = True
        for i in range(len(str(num))):
            if not is_prime:
                break
            num_str = str(num)[:len(num_str) - i]
            if int(num_str) == 1:
                is_prime = False
            elif int(num_str) == 2:
                is_prime = True
            else:
                for j in range(2, int(int(num_str) ** 0.5) + 1):
                    if int(num_str) % j == 0:
                        is_prime = False
                        break
        if is_prime:
            primes.append(num)
    primes.sort(reverse=True)
    return primes