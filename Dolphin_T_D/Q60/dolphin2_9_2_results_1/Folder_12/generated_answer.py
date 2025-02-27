def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[70]
    primes = []
    for number in range(10, x + 1):
        if is_prime(number) and '0' not in str(number):
            trunc = str(number)
            while len(trunc) > 1:
                trunc = trunc[1:-1]
                if not is_prime(int(trunc)):
                    break
            else:
                primes.append(int(number))
    return sorted(primes, reverse=True)