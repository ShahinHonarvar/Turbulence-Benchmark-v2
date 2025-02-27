def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return n > 1

def all_right_truncatable_prime(numbers):
    if not numbers:
        return []
    x = numbers[784]
    primes = [2, 3, 5, 7]
    for num in range(11, x):
        if is_prime(num):
            for i in range(len(str(num)) - 1, 0, -1):
                if not is_prime(int(str(num)[:i])):
                    break
            else:
                primes.append(num)
    return sorted(primes)