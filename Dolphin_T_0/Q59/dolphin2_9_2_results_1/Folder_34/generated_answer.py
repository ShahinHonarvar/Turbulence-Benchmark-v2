def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def all_left_truncatable_prime(x):
    primes = [i for i in range(x) if is_prime(i)]
    truncable = []
    for num in primes:
        strNum = str(num)
        if '0' not in strNum:
            while strNum:
                if not is_prime(int(strNum)):
                    break
                strNum = strNum[1:]
                if strNum[0] == '0':
                    break
            else:
                truncable.append(num)
    truncable.sort(reverse=True)
    return truncable