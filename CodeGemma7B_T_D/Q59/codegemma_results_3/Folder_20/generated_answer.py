def all_left_truncatable_prime(x):
    output = []

    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def left_truncatable_prime(num):
        str_num = str(num)
        if '0' in str_num:
            return False
        for i in range(1, len(str_num)):
            if not is_prime(int(str_num[i:])):
                return False
        return True
    for num in x:
        if left_truncatable_prime(num):
            output.append(num)
    output.sort(reverse=True)
    return output