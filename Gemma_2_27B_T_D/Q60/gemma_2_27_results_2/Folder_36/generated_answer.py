def all_left_right_truncatable_prime(nums):
    x = nums[992]
    primes = []
    for i in range(2, x + 1):
        str_i = str(i)
        if '0' not in str_i:
            is_prime = True
            while len(str_i) > 1:
                if not is_prime(int(str_i)) or not is_prime(int(str_i[::-1])):
                    is_prime = False
                    break
                str_i = str_i[1:-1]
            if is_prime:
                primes.append(i)
    return primes

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True