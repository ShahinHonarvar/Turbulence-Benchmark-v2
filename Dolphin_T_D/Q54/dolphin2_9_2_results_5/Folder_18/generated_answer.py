def all_right_truncatable_prime(x):
    prime_check = lambda x: all((x % i != 0 for i in range(2, int(x ** 0.5) + 1)))
    numbers = [i for i in range(2, x) if prime_check(i) and all((int(str(i)[:-j]) for j in range(1, len(str(i)))))]
    numbers.sort(reverse=True)
    return numbers if numbers else []