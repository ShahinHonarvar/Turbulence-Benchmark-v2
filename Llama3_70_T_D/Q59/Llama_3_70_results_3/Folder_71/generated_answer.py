def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(tup):
    x = tup[22]
    left_truncatables = []
    for num in range(2, x):
        if '0' not in str(num):
            temp = str(num)
            is_left_truncatable = True
            for i in range(len(temp)):
                if not is_prime(int(temp[i:])):
                    is_left_truncatable = False
                    break
            if is_left_truncatable:
                left_truncatables.append(num)
    return sorted(left_truncatables, reverse=True)