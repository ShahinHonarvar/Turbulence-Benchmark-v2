def all_left_truncatable_prime(x):
    prime_nums = [2, 3, 5, 7]
    nums = [i for i in prime_nums if i < x]
    while nums[-1] * 2 < x:
        i = nums[-1] + 2
        while i % 3 == 0 or i % 5 == 0:
            i += 2
        i = int(str(i)[::-1])
        f = True
        while i > 0 and i % 10 != 0 and f:
            if is_prime(i):
                i = int(str(i)[1:])
            else:
                f = False
        if f:
            nums.append(i)
    return sorted(nums)

def is_prime(n):
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            return False
    return True