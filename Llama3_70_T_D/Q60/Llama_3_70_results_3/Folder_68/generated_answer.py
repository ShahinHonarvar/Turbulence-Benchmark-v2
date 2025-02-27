def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):

    def is_left_right_truncatable_prime(n):
        s = str(n)
        if '0' in s:
            return False
        for i in range(len(s)):
            for j in range(i + 1, len(s)):
                if not is_prime(int(s[i:j + 1])):
                    return False
        return True
    x = nums[1]
    left_right_truncatable_primes = [i for i in range(2, x + 1) if is_prime(i) and is_left_right_truncatable_prime(i)]
    return sorted(left_right_truncatable_primes, reverse=True)