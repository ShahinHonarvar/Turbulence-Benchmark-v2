def all_left_truncatable_prime(numbers):
    x = numbers[74]
    primes = []
    for num in range(2, x):
        if num > 9:
            check = int(str(num)[1:] + str(num)[0])
            while check < x and len(str(check)) != 0 and (len(str(check)) != 1):
                if check in primes:
                    pass
                else:
                    for p in primes:
                        if check % p == 0:
                            break
                    else:
                        primes.append(check)
                check = int(str(check)[1:] + str(check)[0])
        elif is_prime(num):
            primes.append(num)
    primes = list(set(primes))
    return sorted(list(map(int, primes)))

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True