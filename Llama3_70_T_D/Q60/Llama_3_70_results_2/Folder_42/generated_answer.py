def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    limit = numbers[64]
    left_right_truncatable_primes = []
    for num in range(11, limit + 1):
        if '0' in str(num):
            continue
        if not is_prime(num):
            continue
        temp_num = str(num)
        left_truncatable = True
        right_truncatable = True
        for _ in range(len(temp_num) - 2):
            temp_num = temp_num[1:]
            if not is_prime(int(temp_num)):
                left_truncatable = False
                break
        temp_num = str(num)
        for _ in range(len(temp_num) - 2):
            temp_num = temp_num[:-1]
            if not is_prime(int(temp_num)):
                right_truncatable = False
                break
        if left_truncatable and right_truncatable:
            left_right_truncatable_primes.append(num)
    return sorted(left_right_truncatable_primes, reverse=True)