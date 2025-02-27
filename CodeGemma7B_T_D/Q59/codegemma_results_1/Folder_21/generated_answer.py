def all_left_truncatable_prime(tp):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def to_int(l):
        n = 0
        for i in l:
            n = n * 10 + i
        return n
    result = []
    x = tp[175]
    for i in range(2, x):
        str_i = str(i)
        if not '0' in str_i and is_prime(i):
            trucatable = True
            for j in range(1, len(str_i)):
                if not is_prime(to_int(list(str_i[j:]))):
                    trucatable = False
                    break
            if trucatable:
                result.append(i)
    return sorted(result)