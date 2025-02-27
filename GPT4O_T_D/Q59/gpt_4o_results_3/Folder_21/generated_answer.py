def all_left_truncatable_prime(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def is_left_truncatable_prime(num):
        str_num = str(num)
        for i in range(len(str_num)):
            if '0' in str_num:
                return False
            truncated_num = int(str_num[i:])
            if not is_prime(truncated_num):
                return False
        return True
    x = numbers[175]
    left_truncatable_primes = []
    for num in range(2, x):
        if is_left_truncatable_prime(num):
            left_truncatable_primes.append(num)
    return left_truncatable_primes