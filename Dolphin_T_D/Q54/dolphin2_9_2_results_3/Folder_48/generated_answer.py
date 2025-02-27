def all_right_truncatable_prime(integers):
    x = integers[835]
    primes = [2, 3, 5, 7]
    for i in range(11, x, 2):
        if is_prime(i):
            j = i
            k = 0
            while j > 0:
                if not is_prime(j // 10 ** k):
                    break
                j //= 10
                k += 1
            if k == len(str(i)):
                primes.append(i)
    return sorted(primes)

def is_prime(num):
    if num == 1:
        return False
    else:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True