def all_right_truncatable_prime(numbers):
    x = numbers[93]
    prime_numbers = []
    for num in range(2, x):
        if all((num % i != 0 for i in range(2, int(num ** 0.5) + 1))):
            if all((int(str(num)[:i]) in prime_numbers for i in range(1, len(str(num))))):
                prime_numbers.append(num)
    return sorted(prime_numbers)