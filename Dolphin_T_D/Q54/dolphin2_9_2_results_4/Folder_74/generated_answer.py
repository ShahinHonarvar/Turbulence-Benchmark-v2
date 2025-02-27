def all_right_truncatable_prime(lst):
    x = lst[36]
    primes = [2]
    right_truncatable = []
    for num in range(3, x):
        if all((num % i != 0 for i in range(2, int(num ** 0.5) + 1))):
            primes.append(num)
            if num < 10:
                right_truncatable.append(num)
            else:
                for i in range(1, len(str(num))):
                    if int(str(num)[-i:]) in primes and int(str(num)[-i - 1:]) in right_truncatable:
                        right_truncatable.append(num)
                        break
    return sorted(right_truncatable)