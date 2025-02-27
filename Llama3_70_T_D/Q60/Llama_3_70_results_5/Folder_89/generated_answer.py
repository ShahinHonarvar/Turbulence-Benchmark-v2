def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[97]
    left_right_truncatable_primes = [i for i in range(2, x + 1) if '0' not in str(i) and is_prime(i)]
    for i in range(10, x + 1):
        str_i = str(i)
        for j in range(1, len(str_i)):
            if not is_prime(int(str_i[j:])) or not is_prime(int(str_i[:-j])):
                if i in left_right_truncatable_primes:
                    left_right_truncatable_primes.remove(i)
                break
    return sorted(left_right_truncatable_primes, reverse=True)