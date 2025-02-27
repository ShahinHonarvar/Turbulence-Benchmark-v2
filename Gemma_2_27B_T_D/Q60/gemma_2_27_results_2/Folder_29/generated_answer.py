def all_left_right_truncatable_prime(nums):
    x = nums[55]
    primes = []
    for i in range(2, x + 1):
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime and '0' not in str(i):
            num_str = str(i)
            is_truncatable = True
            while len(num_str) > 1:
                num_str = num_str[1:-1]
                if int(num_str) < 2 or not all((int(digit) != 0 for digit in num_str)) or (not is_prime1(int(num_str))):
                    is_truncatable = False
                    break
            if is_truncatable:
                primes.append(i)
    return sorted(primes, reverse=True)

def is_prime1(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True