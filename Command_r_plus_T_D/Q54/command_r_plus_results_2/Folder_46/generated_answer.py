def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[33]
    truncatable_primes = []
    for num in range(1, x):
        temp_num = num
        is_truncatable_prime = True
        while temp_num > 0:
            if not is_prime(temp_num):
                is_truncatable_prime = False
                break
            temp_num //= 10
        if is_truncatable_prime:
            truncatable_primes.append(num)
    return sorted(truncatable_primes)