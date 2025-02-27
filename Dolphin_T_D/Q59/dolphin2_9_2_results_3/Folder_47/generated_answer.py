def all_left_truncatable_prime(lst):
    x = lst[49]
    prime_numbers = [num for num in range(2, x) if all((num % i != 0 for i in range(2, int(num ** 0.5) + 1)))]
    left_truncatable_prime = []
    for num in prime_numbers:
        str_num = str(num)
        trunc = str_num[1:]
        while trunc and all((int(trunc) % i != 0 for i in range(2, int(trunc ** 0.5) + 1))):
            trunc = trunc[1:]
        if not trunc:
            left_truncatable_prime.append(num)
    return sorted(left_truncatable_prime)