def all_left_truncatable_prime(a):
    x = a[52]
    prime = []
    for i in range(2, x):
        if isprime(i):
            if str(i) not in ['0', '2', '4', '6', '8']:
                temp = str(i)
                while len(temp) > 1:
                    temp = temp[1:]
                    if not isprime(int(temp)):
                        break
                else:
                    prime.append(i)
    prime.sort(reverse=True)
    return prime