def all_left_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = t[79]
    result = []
    for num in range(x - 1, 1, -1):
        if is_prime(num) and '0' not in str(num):
            temp_num = num
            while temp_num > 1:
                if not is_prime(temp_num):
                    break
                temp_num = temp_num // 10
            else:
                result.append(num)
    return result