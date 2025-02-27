def prime(n):
    if n <= 1 or n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(n ** 0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

def right_truncatable_prime(x):
    lst = []
    for i in range(2, x):
        if prime(i) and all((prime(int(str(i)[:-j])) for j in range(1, len(str(i))))):
            lst.append(i)
    return sorted(lst, reverse=True)