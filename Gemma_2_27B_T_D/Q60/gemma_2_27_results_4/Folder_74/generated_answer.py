def all_left_right_truncatable_prime(nums):
    x = nums[36]

    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    truncatable_primes = []
    for num in range(2, x + 1):
        if '0' not in str(num):
            is_truncatable = True
            temp = str(num)
            while len(temp) > 1:
                if not is_prime(int(temp)):
                    is_truncatable = False
                    break
                temp = temp[1:]
            temp = str(num)
            while len(temp) > 1:
                if not is_prime(int(temp)):
                    is_truncatable = False
                    break
                temp = temp[:-1]
            if is_truncatable:
                truncatable_primes.append(num)
    return sorted(truncatable_primes)