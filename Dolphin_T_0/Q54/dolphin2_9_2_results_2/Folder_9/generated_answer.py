def all_right_truncatable_prime(t):
    x = t[29]
    result = []
    for num in range(2, x):
        if all((num % i != 0 for i in range(2, int(num ** 0.5) + 1))):
            while num != 0:
                if all((num % i != 0 for i in range(2, int(num ** 0.5) + 1))):
                    result.append(num)
                    num //= 10
                else:
                    break
    return sorted(result, reverse=True)