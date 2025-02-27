def all_left_right_truncatable_prime(numbers):
    x = numbers[43]
    primes = []
    for num in range(2, x + 1):
        if all((int(str(num)[:i]) in [2, 3, 5, 7] and int(str(num)[i:]) in [2, 3, 5, 7] for i in range(1, len(str(num))))) and all((int(str(num)[:i]) and int(str(num)[i:]) for i in range(1, len(str(num))))):
            primes.append(num)
    return primes