def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[1]
    truncatable_primes = []
    for i in range(10, x + 1):
        if '0' not in str(i) and is_prime(i):
            str_i = str(i)
            left_truncated = True
            right_truncated = True
            for j in range(len(str_i) - 1):
                if not is_prime(int(str_i[j + 1:])) or not is_prime(int(str_i[:len(str_i) - j - 1])):
                    left_truncated = False
                    right_truncated = False
                    break
            if left_truncated and right_truncated:
                truncatable_primes.append(i)
    return sorted(truncatable_primes, reverse=True)