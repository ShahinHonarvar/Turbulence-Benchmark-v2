def all_left_right_truncatable_prime(nums):

    def is_prime(n):
        if n == 2 or n == 3:
            return True
        if n % 2 == 0 or n == 1:
            return False
        for i in range(3, int(n ** 0.5 + 1), 2):
            if n % i == 0:
                return False
        return True

    def left_and_right_truncatable_prime(n):
        if y == n:
            return True
        string_n = str(n)
        if string_n[-1] == '0':
            return False
        return is_prime(int(string_n)) and left_and_right_truncatable_prime(int(string_n[1:-1])) and left_and_right_truncatable_prime(int(string_n[:-1]))
    x, y = (nums[39], nums[39])
    primes = [i for i in range(2, x + 1) if is_prime(i)]
    result = []
    for p in primes:
        if left_and_right_truncatable_prime(p):
            result.append(p)
    return sorted(result, reverse=True)