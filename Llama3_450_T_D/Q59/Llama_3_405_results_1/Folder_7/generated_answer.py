def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[803]
    truncatable_primes = []
    for num in range(2, x):
        if is_prime(num) and '0' not in str(num):
            truncatable = True
            temp = str(num)
            for j in range(len(temp)):
                if not is_prime(int(temp[j:])):
                    truncatable = False
                    break
            if truncatable:
                truncatable_primes.append(num)
    return sorted(truncatable_primes)