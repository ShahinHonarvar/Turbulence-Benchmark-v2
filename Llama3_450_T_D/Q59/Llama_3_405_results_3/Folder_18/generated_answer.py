def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[429]
    truncatable_primes = set()
    for num in range(11, x):
        if '0' in str(num):
            continue
        if is_prime(num):
            truncatable = True
            temp = str(num)
            for i in range(len(temp)):
                if not is_prime(int(temp[i:])):
                    truncatable = False
                    break
            if truncatable:
                truncatable_primes.add(num)
    return sorted(list(truncatable_primes), reverse=True)