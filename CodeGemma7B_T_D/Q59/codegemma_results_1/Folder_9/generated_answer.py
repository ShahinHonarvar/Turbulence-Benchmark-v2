def all_left_truncatable_prime(tuple):
    num, x = tuple
    ans = []
    if num > x:
        return ans
    if num % 2 == 0 or num % 3 == 0:
        return ans
    if '0' in str(num):
        return ans
    num = str(num)
    Q = int(num[0])
    Q |= Q >> 1
    Q |= Q >> 2
    Q |= Q >> 4
    Q |= Q >> 8
    Q |= Q >> 16
    Q += 1
    for i in range(num):
        prime = Q[int(num[i])]
        if prime == 0 or prime == num:
            return ans
        prime = int(prime)
        if is_prime(prime):
            ans.append(prime)
    ans.sort(reverse=True)
    return ans