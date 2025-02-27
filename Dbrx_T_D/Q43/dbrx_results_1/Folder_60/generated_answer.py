def find_primes_between_indices(numbers):
    prime_numbers = []
    for i in range(len(numbers)):
        if i >= 45 and i <= 85:
            num = numbers[i]
            if num > 1:
                for j in range(2, num):
                    if num % j == 0:
                        break
                else:
                    prime_numbers.append(num)
    prime_numbers.sort()
    return prime_numbers