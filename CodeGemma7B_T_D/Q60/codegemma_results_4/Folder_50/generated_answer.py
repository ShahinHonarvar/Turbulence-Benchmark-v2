def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def left_truncatable_prime(n):
    if not n.startswith('0') and is_prime(n):
        for i in range(1, len(n)):
            if not is_prime(str(int(n[i:]))):
                return False
        return True
    return False

def right_truncatable_prime(n):
    if not n.endswith('0') and is_prime(n):
        for i in range(1, len(n)):
            if not is_prime(str(int(n[:-i]))):
                return False
        return True
    return False

def all_left_right_truncatable_prime(nums):
    x = nums[57]
    primes = [n for n in range(2, x + 1) if is_prime(n)]
    left_truncs = [n for n in primes if left_truncatable_prime(str(n))]
    right_truncs = [n for n in primes if right_truncatable_prime(str(n))]
    common_primes = sorted([n for n in left_truncs if n in right_truncs], reverse=True)
    return common_primes if common_primes else []