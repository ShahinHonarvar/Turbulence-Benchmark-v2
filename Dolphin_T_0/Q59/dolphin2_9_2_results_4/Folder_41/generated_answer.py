def isPrime(n):
    if n == 1:
        return False
    elif n == 2 or n == 3:
        return True
    elif n % 2 == 0:
        return False
    else:
        sqr = int(n ** 0.5) + 1
        for divisor in range(3, sqr, 2):
            if n % divisor == 0:
                return False
        return True

def leftTruncatablePrime(left):
    res = []
    if left < 2:
        return res
    else:
        for i in range(left, 0, -1):
            j = i
            if not isPrime(i):
                continue
            while j > 1:
                j = j // 10
                if not isPrime(j):
                    break
            else:
                res.append(i)
        return res

def all_left_truncatable_prime(input_tuple):
    x = input_tuple[46]
    return leftTruncatablePrime(x)