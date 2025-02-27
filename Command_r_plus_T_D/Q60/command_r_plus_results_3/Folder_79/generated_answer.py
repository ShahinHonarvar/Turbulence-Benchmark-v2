def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def left_right_truncate(n):
    str_n = str(n)
    left_truncate = [int(str_n[i:]) for i in range(len(str_n))]
    right_truncate = [int(str_n[:i]) for i in range(1, len(str_n) + 1)]
    return all((is_prime(i) for i in left_truncate + right_truncate))

def all_left_right_truncatable_prime(numbers):
    start, end = numbers
    truncatable_primes = []
    for num in range(start, end + 1):
        if num > 10 and '0' not in str(num) and left_right_truncate(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes)