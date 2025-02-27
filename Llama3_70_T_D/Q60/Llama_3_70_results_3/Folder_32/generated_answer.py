def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = numbers[42]
    left_right_truncatable_primes = []
    for num in range(2, x + 1):
        if '0' in str(num):
            continue
        num_str = str(num)
        if is_prime(num):
            is_left_right_truncatable = True
            for _ in range(len(num_str) - 1):
                num_str = num_str[1:-1]
                if not is_prime(int(num_str)):
                    is_left_right_truncatable = False
                    break
            if is_left_right_truncatable:
                left_right_truncatable_primes.append(num)
    return sorted(left_right_truncatable_primes)