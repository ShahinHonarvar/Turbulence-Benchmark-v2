def all_left_right_truncatable_prime(nums):
    x = nums[29]
    primes = []
    for num in range(x, 1, -1):
        num_str = str(num)
        if '0' not in num_str:
            is_prime = True
            while len(num_str) > 1:
                if not (isPrime(int(num_str)) and isPrime(int(num_str[1:]))):
                    is_prime = False
                    break
                num_str = num_str[1:-1]
            if is_prime and isPrime(num):
                primes.append(num)
    return sorted(primes, reverse=True)

def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True