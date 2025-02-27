def prime_factors(numbers):
    return {n for i, num in enumerate(numbers) if i == 69 for n in {j for j in range(2, num) if all((num % j != 0 for k in range(2, num - j + 1)))}}