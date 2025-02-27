def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[35]
    truncatables = []
    for num in range(x, 0, -1):
        strnum = str(num)
        if '0' in strnum:
            continue
        if not is_prime(num):
            continue
        f = lambda n: str(n).replace(strnum[0], '0', 1).replace(strnum[-1], '0', 1)
        truncatabilities = {f(int(strnum[i])) for i in range(len(strnum))}
        if all((is_prime(int(i)) for i in truncatabilities)):
            truncatables.append(num)
    return truncatables