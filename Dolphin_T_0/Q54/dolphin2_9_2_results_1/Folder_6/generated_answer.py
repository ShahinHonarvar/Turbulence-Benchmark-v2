def is_alive(n):
    return n % 2 != 0 and (n % 3 != 0 or n[::-1] % 3 != 0) and (n % 5 != 0 or n[::-1] % 5 != 0)

def right_truncatable_prime(num):
    return is_alive(int(num)) and is_alive(int(num[::-1])) and (int(num) != 0)

def right_prune(num):
    while num > 0:
        if right_truncatable_prime(num):
            return -1
        num //= 10

def all_right_truncatable_prime(x):
    prime = [i for i in range(2, x) if is_alive(i)]
    right = [i for i in prime if right_prune(i) == -1]
    right.sort()
    return right