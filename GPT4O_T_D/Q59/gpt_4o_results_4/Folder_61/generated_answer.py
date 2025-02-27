def all_left_truncatable_prime(numbers):
    x = numbers[3]

    def is_prime(num):
        if num <= 1:
            return False
        if num <= 3:
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6
        return True

    def is_left_truncatable_prime(num):
        str_num = str(num)
        if '0' in str_num:
            return False
        while str_num:
            if not is_prime(int(str_num)):
                return False
            str_num = str_num[1:]
        return True
    left_truncatable_primes = [num for num in range(2, x) if is_left_truncatable_prime(num)]
    return sorted(left_truncatable_primes, reverse=True)