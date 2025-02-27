def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def all_right_truncatable_prime(numbers: tuple[int, ...]) -> list[int]:
    right_truncatable_primes = []
    for num in numbers:
        if num >= 10:
            num_str = str(num)
            for i in range(1, len(num_str)):
                if not is_prime(int(num_str[:i])):
                    break
            else:
                if is_prime(num):
                    right_truncatable_primes.append(num)
    right_truncatable_primes.sort()
    return right_truncatable_primes