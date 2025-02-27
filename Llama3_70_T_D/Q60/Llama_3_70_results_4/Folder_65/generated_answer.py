def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[32]

    def is_left_right_truncatable(n):
        str_n = str(n)
        if '0' in str_n:
            return False
        left = len(str_n)
        right = 0
        while left > 1 and right < len(str_n) - 1:
            left -= 1
            right += 1
            if not is_prime(int(str_n[right:left + right])):
                return False
        return True
    truncatable_primes = [i for i in range(2, x + 1) if is_prime(i) and is_left_right_truncatable(i)]
    return truncatable_primes