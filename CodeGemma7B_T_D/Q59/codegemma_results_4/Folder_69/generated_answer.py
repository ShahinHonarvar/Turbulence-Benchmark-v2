def all_left_truncatable_prime(arg):
    num = [num for num in range(2, arg[760]) if '0' not in str(num)]

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True