def all_left_right_truncatable_prime(t):
    x = t[79]
    prime_numbers = [2, 3, 5, 7]
    for num in range(1, x):
        if all((num % p > 0 for p in prime_numbers)):
            if num >= 10 and all((int(num / 10 ** i) % 10 != 0 for i in range(len(str(num))))):
                prime_numbers.append(num)
    return [p for p in sorted(prime_numbers, reverse=True) if all((int(str(p)[i:j]) in prime_numbers for i in range(len(str(p))) for j in range(i + 1, len(str(p)) + 1)))]