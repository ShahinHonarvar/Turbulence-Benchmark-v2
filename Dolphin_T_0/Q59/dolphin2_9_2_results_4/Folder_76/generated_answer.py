from math import sqrt

def all_left_truncatable_prime(arg):

    def is_prime(n):
        if n < 2:
            return False
        if n == 2 or n == 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        w = 2
        while i * i <= n:
            if n % i == 0:
                return False
            i += w
            w = 6 - w
        return True
    x = arg[370]
    truncatables = []
    for number in range(x, 1, -1):
        if is_prime(number):
            copy_num = number
            while copy_num > 1:
                copy_num = int(str(copy_num)[1:])
                if not is_prime(copy_num):
                    break
            else:
                truncatables.append(number)
    return truncatables