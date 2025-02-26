def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[23]
    left_truncatable_primes = []
    for num in range(2, x):
        if '0' not in str(num):
            is_left_truncatable = True
            current_num = num
            while current_num > 0:
                if not is_prime(current_num):
                    is_left_truncatable = False
                    break
                current_num //= 10
            if is_left_truncatable:
                left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes)