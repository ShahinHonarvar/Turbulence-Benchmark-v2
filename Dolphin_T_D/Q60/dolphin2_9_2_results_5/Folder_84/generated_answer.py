def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[630]
    res = [i for i in range(x, -1, -1) if is_prime(i) and (not '0' in str(i)) and (len(str(i)) > 1) and all((is_prime(int(str(i)[1:-1])) for i in range(len(str(i)) - 2, -1, -1)))]
    return res