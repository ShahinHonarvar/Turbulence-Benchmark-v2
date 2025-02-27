def all_left_truncatable_prime(tup):
    x = tup[10]
    prime = [i for i in range(2, x) if all((i % j != 0 for j in range(2, i)))]
    ans = []
    for i in prime:
        if '0' not in str(i):
            temp = i
            while temp > 0:
                if temp in prime:
                    ans.append(temp)
                temp = int(str(temp)[1:])
    return sorted(ans, reverse=True)