def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[177]
    left_truncatable_primes = []
    for num in range(2, x):
        if '0' not in str(num):
            truncatable = True
            num_str = str(num)
            for i in range(1, len(num_str)):
                if not is_prime(int(num_str[i:])):
                    truncatable = False
                    break
            if truncatable and is_prime(num):
                left_truncatable_primes.append(num)
    return left_truncatable_primes