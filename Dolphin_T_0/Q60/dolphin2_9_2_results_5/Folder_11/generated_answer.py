def is_prime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        p = 3
        while p * p <= n:
            if n % p == 0:
                return False
            p += 2
        return True

def all_left_right_truncatable_prime(nums):
    left_right_truncatable = []
    for x in nums:
        for n in range(x, 0, -1):
            if is_prime(n):
                digits = [digit for digit in str(n) if digit != '0']
                left_truncatable = [int(''.join(digits[i:])) for i in range(len(digits) - 1)]
                right_truncatable = [int(''.join(digits[:i + 1])) for i in range(len(digits) - 1)]
                if set(map(is_prime, left_truncatable)).issubset(left_truncatable) and set(map(is_prime, right_truncatable)).issubset(right_truncatable):
                    left_right_truncatable.append(n)
    return sorted(list(set(left_right_truncatable)))