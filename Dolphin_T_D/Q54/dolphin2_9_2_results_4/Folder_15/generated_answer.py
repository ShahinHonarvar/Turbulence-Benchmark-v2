def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[6]
    prime_numbers = []
    for i in range(x - 1, 1, -1):
        n = i
        while n != 0:
            if not is_prime(n):
                break
            n //= 10
        else:
            prime_numbers.append(i)
    return sorted(prime_numbers, reverse=True)