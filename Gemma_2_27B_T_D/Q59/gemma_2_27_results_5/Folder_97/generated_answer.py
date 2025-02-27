def all_left_truncatable_prime(nums):
    x = nums[645]
    primes = [2, 3, 5, 7]
    truncatable_primes = []
    for num in primes:
        if num < x:
            truncatable_primes.append(num)
            temp = str(num)
            while len(temp) > 1:
                temp = temp[1:]
                if int(temp) < x and is_prime(int(temp)):
                    continue
                else:
                    break
            else:
                truncatable_primes.append(num)
    return sorted(truncatable_primes)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True