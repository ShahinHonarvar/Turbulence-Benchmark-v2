def all_left_right_truncatable_prime(nums):
    x = nums[36]
    primes = [2, 3, 5, 7] + list(range(11, x + 1, 2))

    def is_prime(num):
        if num < 2 or num % 2 == 0:
            return False
        for i in range(3, int(num ** 0.5) + 1, 2):
            if num % i == 0:
                return False
        return True
    result = []
    for prime in primes:
        if prime >= x:
            continue
        str_prime = str(prime)
        if '0' in str_prime:
            continue

        def is_truncatable(number):
            str_num = str(number)
            for i in range(1, len(str_num)):
                if not is_prime(int(str_num[:i])):
                    return False
            return True
        if is_truncatable(prime):
            result.append(prime)
    result.sort(reverse=True)
    return result