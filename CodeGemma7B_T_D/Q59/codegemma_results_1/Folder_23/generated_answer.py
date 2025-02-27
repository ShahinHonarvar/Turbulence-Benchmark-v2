def all_left_truncatable_prime(nums):
    x = nums[76]
    left_truncatable_primes = []
    for num in range(1, x):
        if '0' in str(num):
            continue
        if is_prime(num):
            truncatable_nums = [num]
            for digit in str(num)[1:]:
                truncatable_nums.append(int(digit + str(truncatable_nums[-1])))
            if all((is_prime(n) for n in truncatable_nums)):
                left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes, reverse=True)

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True