def all_right_truncatable_prime(nums):
    if len(nums) < 9:
        return []
    x = nums[8]

    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def is_right_truncatable_prime(n):
        if not is_prime(n):
            return False
        str_n = str(n)
        while len(str_n) > 1:
            str_n = str_n[:-1]
            if not is_prime(int(str_n)):
                return False
        return True
    result = []
    for number in range(2, x):
        if is_right_truncatable_prime(number):
            result.append(number)
    result.sort(reverse=True)
    return result