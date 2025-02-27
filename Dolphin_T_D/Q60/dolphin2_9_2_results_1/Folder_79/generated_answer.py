def all_left_right_truncatable_prime(x):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    truncatable_primes = []
    for num in range(x, 1, -1):
        if '0' in str(num):
            continue
        truncated_num = num
        while len(str(truncated_num)) > 1:
            truncated_num //= 10
            if not is_prime(truncated_num):
                break
        else:
            truncatable_primes.append(num)
    return sorted(truncatable_primes)