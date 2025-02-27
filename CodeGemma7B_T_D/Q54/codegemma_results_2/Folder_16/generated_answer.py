def all_right_truncatable_prime(arg):
    return sorted([i for i in range(2, arg[792]) if all((str(i)[-j] in '2357' for j in range(1, len(str(i))))) and all((is_prime(i) and is_prime(int(str(i)[:-j])) for j in range(1, len(str(i)))))], reverse=True)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True