def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[3]
    truncatable_primes = []
    for num in range(x, 11, -1):
        if '0' in str(num):
            continue
        is_left_right_truncatable = True
        for length in range(len(str(num)), 0, -1):
            left_trunc = int(str(num)[length - 1:])
            right_trunc = int(str(num)[:length])
            curr = left_trunc
            while curr > 10:
                if not is_prime(curr):
                    is_left_right_truncatable = False
                    break
                curr //= 10
            curr = right_trunc
            while curr > 10:
                if not is_prime(curr):
                    is_left_right_truncatable = False
                    break
                curr //= 10
            if not is_left_right_truncatable:
                break
        if is_left_right_truncatable and is_prime(num) and is_prime(int(str(num)[0])) and is_prime(int(str(num)[-1])):
            truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)