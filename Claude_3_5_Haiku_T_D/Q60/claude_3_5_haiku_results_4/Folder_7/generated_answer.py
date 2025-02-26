def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[803]
    truncatable_primes = []
    for num in range(2, x + 1):
        if '0' in str(num):
            continue
        if not is_prime(num):
            continue
        left_right_truncatable = True
        temp_num = num
        while temp_num > 0:
            if not is_prime(temp_num):
                left_right_truncatable = False
                break
            temp_num //= 10
        temp_num = num
        num_str = str(temp_num)
        while len(num_str) > 1:
            num_str = num_str[1:]
            if not is_prime(int(num_str)):
                left_right_truncatable = False
                break
        if left_right_truncatable:
            truncatable_primes.append(num)
    return sorted(truncatable_primes)