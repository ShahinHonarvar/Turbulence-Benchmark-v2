def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def right_truncatable_prime(t):
    nums = []
    x = t[35]
    for i in range(2, x):
        if is_prime(i):

            def check(i):
                n = i
                while n:
                    if not is_prime(n):
                        return False
                    n //= 10
                return True
            if check(i):
                nums.append(i)
    return sorted(nums, reverse=True) if nums else []