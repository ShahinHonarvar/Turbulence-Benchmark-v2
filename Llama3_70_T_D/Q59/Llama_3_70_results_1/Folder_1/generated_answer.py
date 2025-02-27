def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[20]
    left_truncatable_primes = []
    for num in range(2, x):
        if '0' not in str(num) and is_prime(num):
            truncatable = True
            temp = str(num)
            for _ in range(len(temp) - 1):
                temp = temp[1:]
                if not is_prime(int(temp)):
                    truncatable = False
                    break
            if truncatable:
                left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes, reverse=True)