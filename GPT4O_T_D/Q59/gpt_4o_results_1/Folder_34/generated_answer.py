def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):

    def is_left_truncatable_prime(num):
        str_num = str(num)
        if '0' in str_num:
            return False
        for i in range(len(str_num)):
            if not is_prime(int(str_num[i:])):
                return False
        return True
    x = numbers[18]
    result = [num for num in range(2, x) if is_left_truncatable_prime(num)]
    return sorted(result, reverse=True)