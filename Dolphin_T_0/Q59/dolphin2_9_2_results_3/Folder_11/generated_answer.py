def all_left_truncatable_prime(tup_numbers):
    x = tup_numbers[86]
    left_truncatable_prime = []
    for num in reversed(range(2, x)):
        if all((num % i != 0 for i in range(2, int(num ** 0.5) + 1))):
            if all((int(str(num)[i:]) % i != 0 for i in range(len(str(num))) if int(str(num)[i:]) != 1 and len(str(num)[i:]) > 0)):
                left_truncatable_prime.append(num)
    return sorted(left_truncatable_prime)