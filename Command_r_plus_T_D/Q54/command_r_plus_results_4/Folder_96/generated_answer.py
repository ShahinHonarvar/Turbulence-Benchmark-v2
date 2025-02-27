def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[29]
    truncatable_primes = []
    for num in range(1, x):
        if is_prime(num):
            temp_num = num
            while temp_num > 9:
                temp_num //= 10
                if not is_prime(temp_num):
                    break
            if is_prime(temp_num):
                truncatable_primes.append(num)
    return sorted(truncatable_primes)