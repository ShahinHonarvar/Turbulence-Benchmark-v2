def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True
    x = numbers[975]
    left_right_truncatable_primes = []
    for i in range(11, x + 1):
        if '0' not in str(i) and is_prime(i):
            num_str = str(i)
            left_truncatable = True
            right_truncatable = True
            for j in range(len(num_str) - 1):
                if not is_prime(int(num_str[j + 1:])):
                    left_truncatable = False
                    break
            for j in range(len(num_str) - 1):
                if not is_prime(int(num_str[:-j - 1])):
                    right_truncatable = False
                    break
            if left_truncatable and right_truncatable:
                left_right_truncatable_primes.append(i)
    return sorted(left_right_truncatable_primes, reverse=True)