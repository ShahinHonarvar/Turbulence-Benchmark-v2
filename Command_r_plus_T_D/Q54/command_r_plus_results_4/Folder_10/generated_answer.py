def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[38]
    truncatable_primes = []
    for num in range(1, x):
        temp_num = num
        while temp_num > 0:
            if not is_prime(temp_num):
                break
            temp_num //= 10
        if temp_num == 0 and is_prime(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)