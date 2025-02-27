def all_left_right_truncatable_prime(nums):
    x = nums[1]

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

    def is_truncatable_prime(num):
        str_num = str(num)
        if '0' in str_num:
            return False
        while len(str_num) > 1:
            str_num = str_num[1:]
            if not is_prime(int(str_num)):
                return False
        str_num = str(num)
        while len(str_num) > 1:
            str_num = str_num[:-1]
            if not is_prime(int(str_num)):
                return False
        return True
    truncatable_primes = []
    for num in range(10, x + 1):
        if is_prime(num) and is_truncatable_prime(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)