def all_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = numbers[93]
    truncatable_primes = []
    for num in range(2, x):
        if is_prime(num):
            str_num = str(num)
            truncatable = True
            for i in range(len(str_num) - 1, 0, -1):
                truncated_num = int(str_num[:i])
                if not is_prime(truncated_num):
                    truncatable = False
                    break
            if truncatable:
                truncatable_primes.append(num)
    return sorted(truncatable_primes)