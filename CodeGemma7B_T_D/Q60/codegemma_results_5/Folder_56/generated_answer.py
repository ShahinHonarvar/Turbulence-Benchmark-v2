def all_left_right_truncatable_prime(n):
    i = 5
    list = []
    while i <= n:
        if '0' in str(i):
            i += 2
            continue
        elif isPrime(i):
            j = 0
            k = len(str(i)) - 1
            while j <= k and isPrime(int(str(i)[j:])):
                if j == k and isPrime(int(str(i)[j:])):
                    list.append(i)
                j += 1
                k -= 1
        i += 2
    return sorted(list)

def isPrime(n):
    if n < 2:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True