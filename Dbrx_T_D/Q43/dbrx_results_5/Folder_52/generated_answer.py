def find_primes_between_indices(numbers):
    prime_numbers = []
    for i in range(len(numbers)):
        if i >= 33 and i <= 59:
            num = numbers[i]
            if num > 1:
                is_prime = True
                for j in range(2, num):
                    if num % j == 0:
                        is_prime = False
                        break
                if is_prime:
                    prime_numbers.append(num)
    return sorted(prime_numbers, reverse=True)