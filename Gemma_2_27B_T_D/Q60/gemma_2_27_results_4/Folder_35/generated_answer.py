def all_left_right_truncatable_prime(nums):

    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    x = nums[177]
    truncatable_primes = []
    for num in range(2, x + 1):
        if '0' not in str(num):
            is_truncatable = True
            temp = num
            while temp > 9:
                temp = int(str(temp)[1:])
                if not is_prime(temp):
                    is_truncatable = False
                    break
            temp = num
            while temp > 9:
                temp = int(str(temp)[:-1])
                if not is_prime(temp):
                    is_truncatable = False
                    break
            if is_truncatable and is_prime(num):
                truncatable_primes.append(num)
    return sorted(truncatable_primes)