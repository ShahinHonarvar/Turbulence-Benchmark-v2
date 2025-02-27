def all_right_truncatable_prime(i):
    x = i[36]
    li = [2, 3, 5, 7]
    for m in range(10, x):
        if all((m % n != 0 for n in range(2, int(m ** 0.5 + 1)))):
            n = m
            while n:
                li.append(n)
                n //= 10
    li.append(x)
    li = list(set([i for i in li if all((str(i) in str(x) and x % i != 0 for x in range(2, i)))]))
    li.sort(reverse=True)
    return li