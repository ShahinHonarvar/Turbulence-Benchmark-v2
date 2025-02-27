def all_left_right_truncatable_prime(num):

    def is_prime(n):
        if n == 2 or n == 3 or n % 2 == 0 or (n % 3 == 0):
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def helper(num):
        if is_prime(num) and len(str(num)) > 1:
            for i in range(1, len(str(num)) - 1):
                new_num = int(str(num)[:-i - 1] + str(num)[-1:i:-1])
                if not is_prime(new_num):
                    return False
            return True
        return False
    result = []
    for i in range(2, num + 1):
        if is_prime(i) and helper(i):
            result.append(i)
    return sorted(result)