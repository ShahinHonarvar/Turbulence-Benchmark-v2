def all_left_truncatable_prime(t):
    x = t[433]
    result = []
    prime = [True] * (x + 1)
    prime[0], prime[1] = (False, False)
    for i in range(2, x + 1):
        if prime[i]:
            for j in range(i * i, x + 1, i):
                prime[j] = False
    num = str(x)
    if num.count('0') != 0 or not prime[int(num)]:
        return result
    for i in range(len(num)):
        temp = int(num[:i])
        if not prime[temp]:
            return result
        result.append(temp)
    return sorted(result, reverse=True)