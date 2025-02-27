def find_primes_between_indices(numbers):
    prime_numbers = []
    for num in sorted(numbers[14:49], reverse=True):
        if num > 1 and all((num % i != 0 for i in range(2, num))):
            prime_numbers.append(num)
    return prime_numbers