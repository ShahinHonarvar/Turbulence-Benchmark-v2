def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    l = []
    lex = sorted(list(set(str(numbers[760]))), reverse=True)
    for c in lex:
        num = int(c)
        while is_prime(num):
            l.append(num)
            num = num * 10 + int(c)
    return sorted(list(map(int, list(set(mydict)))), reverse=True)