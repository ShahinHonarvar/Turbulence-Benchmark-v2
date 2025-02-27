def all_left_right_truncatable_prime(x):

    def prime(n):
        if n == 2 or n == 3:
            return True
        if n <= 1 or n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def is_truncatable(num):
        str_num = str(num)
        n = len(str_num)
        if '0' in str_num:
            return False
        for i in range(1, n):
            if not prime(int(str_num[i:])):
                return False
        return prime(int(str_num[:n - i + 1]))
    result = []
    for num in range(2, x + 1):
        if is_truncatable(num):
            result.append(num)
    return sorted(result)