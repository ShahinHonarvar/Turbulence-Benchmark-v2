def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[177]
    left_right_truncatable_primes = []
    for num in range(11, x + 1):
        if '0' in str(num):
            continue
        if is_prime(num):
            truncations = [str(num)[i:j] for i in range(len(str(num))) for j in range(i + 1, len(str(num)) + 1)]
            if all((is_prime(int(trunc)) for trunc in truncations)):
                left_right_truncatable_primes.append(num)
    return sorted(left_right_truncatable_primes)