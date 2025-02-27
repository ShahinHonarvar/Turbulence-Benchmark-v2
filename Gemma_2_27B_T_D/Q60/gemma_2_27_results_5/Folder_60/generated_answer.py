def all_left_right_truncatable_prime(nums):
    x = nums[87]
    primes = []
    for i in range(2, x + 1):
        s = str(i)
        if '0' not in s and all((int(s[j:]) in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97] or is_prime(int(s[j:])) for j in range(len(s)))):
            primes.append(i)
    return primes

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True