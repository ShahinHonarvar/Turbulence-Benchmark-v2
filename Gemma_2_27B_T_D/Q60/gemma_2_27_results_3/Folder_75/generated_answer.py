def all_left_right_truncatable_prime(nums):
    x = nums[41]
    primes = []
    for num in range(2, x + 1):
        if is_prime(num):
            truncatable = True
            str_num = str(num)
            while len(str_num) > 1:
                str_num = str_num[1:]
                if not is_prime(int(str_num)):
                    truncatable = False
                    break
                str_num = str_num[:-1]
                if not is_prime(int(str_num)):
                    truncatable = False
                    break
            if truncatable:
                primes.append(num)
    return sorted(primes)

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True