def all_right_truncatable_prime(x):
    prime = [True] * (x + 1)
    prime[0] = prime[1] = False
    for i in range(2, int(x ** 0.5) + 1):
        if prime[i]:
            for j in range(i * i, x + 1, i):
                prime[j] = False
    result = []
    for num in range(x - 1, 2, -1):
        if prime[num]:
            is_truncatable = True
            for digit in range(1, len(str(num))):
                if not prime[int(str(num)[:-digit])]:
                    is_truncatable = False
                    break
            if is_truncatable:
                result.append(num)
    return sorted(result, reverse=True) if result else []