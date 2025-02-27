def all_right_truncatable_prime(t):

    def is_prime(n):
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    n = t[88]
    prime_set, res = (set(), [])
    for num in range(1, n):
        if is_prime(num):
            temp = num
            while temp != 0:
                if temp not in prime_set:
                    break
                temp //= 10
            if temp == 0:
                prime_set.add(num)
                res.append(num)
    if not res:
        return []
    return sorted(res)