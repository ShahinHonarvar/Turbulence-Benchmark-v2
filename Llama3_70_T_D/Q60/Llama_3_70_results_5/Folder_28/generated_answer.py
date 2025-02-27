def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[19]
    left_right_truncatable_primes = [i for i in range(11, x + 1) if '0' not in str(i) and all((is_prime(int(str(i)[j:len(str(i)) - k])) for j in range(len(str(i))) for k in range(len(str(i))) if j + k < len(str(i)) and len(str(i)[j:len(str(i)) - k]) >= 2))]
    two_digit_primes = [i for i in range(10, x + 1) if is_prime(i)]
    return sorted(list(set(left_right_truncatable_primes + two_digit_primes)))