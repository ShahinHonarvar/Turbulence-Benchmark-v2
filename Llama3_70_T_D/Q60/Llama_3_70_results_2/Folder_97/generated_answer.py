def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[645]
    left_right_truncatable_primes = set()
    for num in range(2, x + 1):
        if '0' not in str(num):
            str_num = str(num)
            left_right_truncatable = True
            for i in range(len(str_num)):
                if not is_prime(int(str_num[i:])) or not is_prime(int(str_num[:len(str_num) - i])):
                    left_right_truncatable = False
                    break
            if left_right_truncatable and is_prime(num):
                left_right_truncatable_primes.add(num)
    return sorted(list(left_right_truncatable_primes))