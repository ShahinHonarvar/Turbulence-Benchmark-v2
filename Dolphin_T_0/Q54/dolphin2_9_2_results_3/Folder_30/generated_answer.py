def all_right_truncatable_prime(t):
    x = t[37]
    prime_numbers = []
    for i in range(x):
        if i < 10:
            if all((i % int(i) != 0 for i in str(i - 1))):
                prime_numbers.append(i)
        elif all((i % int(i) != 0 for i in str(i))):
            prime_numbers.append(i)
    if not prime_numbers:
        return []
    else:
        prime_numbers.sort(reverse=True)
        return prime_numbers