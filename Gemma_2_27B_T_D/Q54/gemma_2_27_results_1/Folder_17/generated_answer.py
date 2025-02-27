def all_right_truncatable_prime(t):
    x = t[36]
    primes = []
    for i in range(2, x):
        if all((int(str(i)[:-j]) == 0 or int(str(i)[:-j]) in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97] for j in range(1, len(str(i))))):
            primes.append(i)
    return sorted(primes, reverse=True)