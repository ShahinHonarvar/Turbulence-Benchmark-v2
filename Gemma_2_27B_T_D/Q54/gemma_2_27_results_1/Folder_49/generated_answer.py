def all_right_truncatable_prime(nums):
    x = nums[14]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    prime_list = []
    for i in range(2, x):
        if is_prime(i):
            right_truncatable = True
            n = str(i)
            while len(n) > 1:
                n = n[:-1]
                if not is_prime(int(n)):
                    right_truncatable = False
                    break
            if right_truncatable:
                prime_list.append(i)
    return sorted(prime_list)