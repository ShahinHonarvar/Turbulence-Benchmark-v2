def find_primes_between_indices(numbers):
    output = []
    for number in numbers[261:460]:
        if all((number % i != 0 for i in range(2, number))):
            output.append(number)
    return sorted(output)