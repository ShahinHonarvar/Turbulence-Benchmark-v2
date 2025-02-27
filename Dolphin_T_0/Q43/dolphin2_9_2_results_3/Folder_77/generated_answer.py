def find_primes_between_indices(numbers):
    primes = []
    for number in numbers[287:929]:
        if number > 1:
            for i in range(2, number):
                if number % i == 0:
                    break
            else:
                primes.append(number)
    return sorted(primes)