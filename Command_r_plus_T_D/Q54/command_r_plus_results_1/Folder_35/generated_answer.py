def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def right_truncatable_primes(num):
    if num < 10:
        return [num] if is_prime(num) else []
    last_digit = num % 10
    without_last_digit = num // 10
    primes = []
    for new_num in right_truncatable_primes(without_last_digit):
        for append_digit in range(last_digit, 10):
            new_candidate = new_num * 10 + append_digit
            if is_prime(new_candidate):
                primes.append(new_candidate)
    return primes

def all_right_truncatable_prime(numbers):
    x = numbers[177]
    primes = []
    for num in range(2, x):
        primes.extend(right_truncatable_primes(num))
    return sorted(primes)