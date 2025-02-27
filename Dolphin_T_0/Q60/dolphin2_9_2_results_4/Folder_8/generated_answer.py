def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[41]
    primes = [2, 3, 5, 7]
    for i in range(11, x + 1, 2):
        if all((str(i)[j] != '0' and is_prime(int(str(i)[1:-1])) for j in range(len(str(i))))):
            primes.append(i)
    primes.sort(reverse=True)
    return primes