def all_left_right_truncatable_prime(x):
    l = []
    for i in range(2, int(x / 2) + 1):
        if i % 10 == 0:
            continue

        def isprime(i):
            if i in [2, 3, 5, 7]:
                return True
            elif i % 2 == 0 or i % 3 == 0 or i % 5 == 0 or (i % 7 == 0):
                return False
            n = i % 10
            i //= 10
            while i > 0:
                if i % 10 % n == 0:
                    return False
                i //= 10
            return True
        if i in l:
            continue
        if isprime(i):
            l1 = []
            t = i

            def helper(t):
                if t % 10 == 0 or t in [2, 3, 5, 7]:
                    l1.append(t)
                elif t // 10 != 0 and t % 10 != 0:
                    l1.append(t)
                    helper(t // 10)
            helper(i)
            l.extend(l1)
            if l1:
                for j in l1:
                    l.append(j // 10)
    m = []
    for i in l:
        if i in [2, 3, 5, 7]:
            continue

        def isprime(i):
            if i % 10 == 0:
                return False
            elif i in [2, 3, 5, 7]:
                return True
            elif i % 2 == 0 or i % 3 == 0 or i % 5 == 0 or (i % 7 == 0):
                return False
            n = i % 10
            i //= 10
            while i > 0:
                if i % 10 % n == 0:
                    return False
                i //= 10
            return True
        if isprime(i):
            m.append(i)
    m.sort(reverse=True)
    return m