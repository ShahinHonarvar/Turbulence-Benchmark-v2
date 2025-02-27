def left_truncatable_prime(n):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_left_truncatable_prime(num):
        str_num = str(num)
        for i in range(len(str_num)):
            if not is_prime(int(str_num[i:])):
                return False
        return True
    x = n[24]
    result = []
    for i in range(2, x):
        if '0' not in str(i) and is_left_truncatable_prime(i):
            result.append(i)
    return result

def all_left_truncatable_prime(n):
    return sorted(left_truncatable_prime(n))