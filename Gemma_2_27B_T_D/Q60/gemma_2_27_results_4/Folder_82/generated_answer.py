def all_left_right_truncatable_prime(nums):
    x = nums[69]
    primes = []
    for num in range(x, 1, -1):
        if num > 9 and '0' not in str(num):
            is_prime = True
            n = num
            while n > 9:
                n = int(str(n)[1:])
                if not is_prime_number(n):
                    is_prime = False
                    break
            n = num
            while n > 9:
                n = int(str(n)[:-1])
                if not is_prime_number(n):
                    is_prime = False
                    break
            if is_prime and is_prime_number(num):
                primes.append(num)
    return sorted(primes, reverse=True)

def is_prime_number(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True