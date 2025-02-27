from math import sqrt as s

def all_left_truncatable_prime(tu):
    prime = [True for i in range(10 ** 4 + 1)]
    prime[0], prime[1] = (False, False)
    for i in range(2, int(s(len(prime))) + 1):
        if prime[i]:
            for j in range(2 * i, len(prime), i):
                prime[j] = False
    l = []
    for i in tu:
        if prime[i]:
            for j in str(i)[:-1]:
                if j == '0' or not prime[int(j)]:
                    break
            else:
                l.append(i)
    return sorted(l, reverse=True)