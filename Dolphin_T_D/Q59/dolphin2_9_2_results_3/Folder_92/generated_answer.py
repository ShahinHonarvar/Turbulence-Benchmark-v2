def all_left_truncatable_prime(n):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, num):
            if num % i == 0:
                return False
        return True
    x = n[7]
    res_list = []
    for num in range(2, x):
        if is_prime(num):
            temp = num
            while temp != 0:
                if not is_prime(temp):
                    break
                temp //= 10
            else:
                res_list.append(num)
    return sorted(res_list)