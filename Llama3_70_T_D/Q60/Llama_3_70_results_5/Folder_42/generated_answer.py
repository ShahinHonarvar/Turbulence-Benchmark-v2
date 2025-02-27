def all_left_right_truncatable_prime(nums):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    truncatable_primes = []
    x = nums[64]
    for num in range(11, x + 1):
        str_num = str(num)
        if '0' in str_num:
            continue
        prime = True
        length = len(str_num)
        for i in range(1, length):
            if not is_prime(int(str_num[i:])) or not is_prime(int(str_num[:-i])):
                prime = False
                break
        if prime:
            truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)