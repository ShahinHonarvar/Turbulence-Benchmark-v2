def all_right_truncatable_prime(numbers):
    x = numbers[85]
    primes = []
    for number in range(2, x):
        if all((number % i != 0 for i in range(2, int(number ** 0.5) + 1))):
            for digit in str(number):
                number = number // 10
                if number == 0:
                    primes.append(int(digit))
                elif all((number % i != 0 for i in range(2, int(number ** 0.5) + 1))):
                    continue
                else:
                    break
    return sorted(primes)