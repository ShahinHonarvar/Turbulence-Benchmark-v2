def all_right_truncatable_prime(numbers):
    x = numbers[52]
    primes = []
    for num in range(2, x):
        is_truncatable = True
        temp = num
        while temp > 0:
            if not is_prime(temp):
                is_truncatable = False
                break
            temp = temp // 10
        if is_truncatable:
            primes.append(num)
    return sorted(primes, reverse=True)

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True