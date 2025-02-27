def all_left_right_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def truncate_left(n):
        return int(str(n)[1:])

    def truncate_right(n):
        return int(str(n)[:-1])
    x = t[126]
    lst = []
    for num in range(x, 1, -1):
        if '0' not in str(num) and is_prime(num):
            temp = num
            while temp > 0:
                if not is_prime(temp):
                    break
                temp = truncate_left(temp)
                if temp < 10:
                    if is_prime(temp):
                        lst.append(num)
                    break
            temp = num
            while temp > 0:
                if not is_prime(temp):
                    break
                temp = truncate_right(temp)
                if temp < 10:
                    if is_prime(temp):
                        lst.append(num)
                    break
    return sorted(lst, reverse=True)