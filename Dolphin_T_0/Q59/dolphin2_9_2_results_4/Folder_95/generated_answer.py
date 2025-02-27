def all_left_truncatable_prime(nums):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    num = nums[77]
    primes = [2, 3, 5, 7]
    nums.append(1)
    nums.sort()
    for i in range(3, num):
        str_i = str(i)
        if '0' not in str_i:
            is_truncatable = True
            for j in range(len(str_i)):
                if not is_prime(int(str_i[j:])):
                    is_truncatable = False
                    break
            if is_truncatable:
                primes.append(i)
    return primes