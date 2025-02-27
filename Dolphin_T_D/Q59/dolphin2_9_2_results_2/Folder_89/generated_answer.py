def all_left_truncatable_prime(check):
    x = check[97]
    prime_numbers = []
    for num in range(x, 1, -1):
        if all((num % i != 0 for i in range(2, num))):
            truncated = num
            while truncated > 0:
                if not all((truncated % i != 0 for i in range(2, truncated))):
                    break
                truncated //= 10
            else:
                prime_numbers.append(num)
    return sorted(prime_numbers, reverse=True)