def all_left_truncatable_prime(n):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def remove_leading_digit(num):
        return int(str(num)[1:])
    left_truncatable_primes = []
    for num in range(n - 1, 0, -1):
        if not str(num).startswith('0') and is_prime(num):
            current_num = num
            while current_num > 10:
                current_num = remove_leading_digit(current_num)
                if not is_prime(current_num):
                    break
            else:
                left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes, reverse=True)