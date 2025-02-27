def all_left_right_truncatable_prime(tup):
    if tup[98] < 3:
        return []
    b = []
    for i in range(2, tup[98] + 1):
        if '0' not in str(i):
            if prime(i):
                for j in range(1, len(str(i))):
                    if prime(int(str(i)[:-j])):
                        if prime(int(str(i)[j:])):
                            b.append(i)
    return sorted(b)

def prime(a):
    if a % 2 == 0 or a % 3 == 0 or a % 5 == 0 or (a % 7 == 0):
        return False
    return True