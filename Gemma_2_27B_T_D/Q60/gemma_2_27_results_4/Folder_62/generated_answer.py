def all_left_right_truncatable_prime(nums):
    x = nums[70]
    primes = []
    for num in range(2, x + 1):
        if str(0) not in str(num):
            is_prime = True
            temp = num
            while temp > 9:
                temp //= 10
                if not is_prime_number(temp):
                    is_prime = False
                    break
            temp = num
            while temp > 9:
                temp %= 10 ** int(len(str(temp)) / 2)
                if not is_prime_number(temp):
                    is_prime = False
                    break
            if is_prime:
                primes.append(num)
    return sorted(primes)

def is_prime_number(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True