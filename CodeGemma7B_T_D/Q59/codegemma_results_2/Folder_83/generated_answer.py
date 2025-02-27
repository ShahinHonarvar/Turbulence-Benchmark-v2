def all_left_truncatable_prime(num):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def left_truncatable(n):
        str_num = str(n)
        for i in range(len(str_num)):
            if str_num[i] == '0' or not is_prime(int(str_num[i:])):
                return False
        return True
    result = []
    for n in range(2, x):
        if left_truncatable(n):
            result.append(n)
    return sorted(result)