def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    max_divisor = int(n ** 0.5) + 1
    for d in range(3, max_divisor, 2):
        if n % d == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[175]
    right_truncatable_primes = []
    for num in range(10, x):
        str_num = str(num)
        is_right_truncatable_prime = True
        for i in range(len(str_num)):
            if not is_prime(int(str_num[:len(str_num) - i])):
                is_right_truncatable_prime = False
                break
        if is_right_truncatable_prime:
            right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes)