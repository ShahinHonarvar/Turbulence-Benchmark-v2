def all_right_truncatable_prime(tup):
    x = tup[71]
    right_truncatable_prime = []
    for i in range(x):
        for j in range(2, i):
            if i % j == 0:
                continue
        for j in range(1, 10):
            num = i % 10 ** j
            if num not in prime:
                break
            if is_prime(num):
                right_truncatable_prime.append(i)
                break
    return sorted(right_truncatable_prime, reverse=True)