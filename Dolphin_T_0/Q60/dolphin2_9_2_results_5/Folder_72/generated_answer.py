def all_left_right_truncatable_prime(tup):

    def is_prime(n):
        if n == 2:
            return True
        elif n % 2 == 0:
            return False
        i = 3
        while i * i <= n:
            if n % i == 0:
                return False
            i += 2
        return True
    x = tup[31]
    left_right_truncatable = []
    for num in range(x, 0, -1):
        if '0' in str(num) or not is_prime(num):
            continue
        temp = num
        while temp >= 10:
            if not is_prime(temp):
                break
            temp = int(str(temp)[1:-1])
        else:
            left_right_truncatable.append(num)
    return sorted(left_right_truncatable, reverse=True)