from math import sqrt

def all_left_right_truncatable_prime(x):
    all_trun = []
    list_prime = []
    for i in range(1, x):
        number = str(i)
        if number.count('0') == 0 and is_prime(2, int(number), i) and is_prime(2, int(number[0]), i) and is_prime(2, int(number[-1]), i):
            list_prime.append(number)
    for i in list_prime:
        number = int(i)
        if is_prime(2, number, number):
            all_trun.append(number)
    if not all_trun:
        return []
    return sorted(all_trun)

def is_prime(a, x, n):
    if n <= a:
        return False
    if n == x:
        return True
    if n % a == 0:
        return False
    return is_prime(a + 1, x, n)