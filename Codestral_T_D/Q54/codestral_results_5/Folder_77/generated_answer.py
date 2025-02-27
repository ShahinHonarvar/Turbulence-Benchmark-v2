def all_right_truncatable_prime(numbers):
    x = numbers[767]
    right_truncatable_primes = []
    for num in range(x - 1, 1, -1):
        if is_prime(num):
            truncated_num = num
            while truncated_num > 0:
                truncated_num = truncated_num // 10
                if not is_prime(truncated_num):
                    break
            else:
                right_truncatable_primes.append(num)
    right_truncatable_primes.sort(reverse=True)
    return right_truncatable_primes

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True