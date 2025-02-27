from math import sqrt

def all_right_truncatable_prime(args):

    def is_prime(n):
        for i in range(2, round(sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    def right_truncatable(n):
        num = str(n)
        list_prime = []
        for i in range(len(num)):
            num = num[:-1]
            if is_prime(int(num)):
                list_prime.append(int(num))
        return list_prime
    x = args[370]
    list_prime = []
    for i in range(2, x):
        if is_prime(i):
            if right_truncatable(i):
                list_prime.extend(right_truncatable(i))
    list_prime.sort(reverse=True)
    return list_prime