def all_left_truncatable_prime(t):
    x = t[3]
    primes = []
    for num in range(x - 1, 0, -1):
        if num > 1 and all((num % i != 0 for i in range(2, int(num ** 0.5) + 1))):
            temp = num
            while temp != 0:
                if temp % 10 == 0:
                    break
                if temp != num and (not all((temp % i != 0 for i in range(2, int(temp ** 0.5) + 1)))):
                    break
                temp //= 10
            else:
                primes.append(num)
    return primes