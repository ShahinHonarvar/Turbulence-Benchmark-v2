def all_right_truncatable_prime(numbers):
    x = numbers[31]
    primes = [i for i in range(2, x) if all((int(str(i)[:j]) in set([2, 3, 5, 7]) or all((int(str(i)[:j]) % k != 0 for k in range(3, int(int(str(i)[:j]) ** 0.5) + 1, 2))) for j in range(1, len(str(i)))))]
    return sorted(primes, reverse=True)