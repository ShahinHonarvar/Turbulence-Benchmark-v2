def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(nums):
    x = nums[89]

    def is_left_truncatable(n):
        n = str(n)
        for i in range(len(n)):
            if not is_prime(int(n[i:])):
                return False
        return True
    result = [i for i in range(10, x) if '0' not in str(i) and is_prime(i) and is_left_truncatable(i)]
    return sorted(result, reverse=True)