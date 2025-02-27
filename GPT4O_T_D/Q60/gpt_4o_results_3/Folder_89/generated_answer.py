def all_left_right_truncatable_prime(numbers):
    x = numbers[97]

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

    def is_left_right_truncatable(num):
        str_num = str(num)
        if '0' in str_num:
            return False
        for i in range(len(str_num)):
            left_truncated = int(str_num[i:]) if i < len(str_num) - 1 else int(str_num[i])
            right_truncated = int(str_num[:len(str_num) - i]) if i > 0 else int(str_num[len(str_num) - i:])
            if not is_prime(left_truncated) or not is_prime(right_truncated):
                return False
        return True
    truncatable_primes = [num for num in range(2, x + 1) if is_prime(num) and is_left_right_truncatable(num)]
    return sorted(truncatable_primes, reverse=True)