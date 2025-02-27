from math import sqrt

def find_primes_between_indices(numbers):
    prime_list = []
    for number in numbers[29:98]:
        if number <= 1:
            continue
        is_prime = True
        for i in range(2, int(sqrt(number)) + 1):
            if number % i == 0:
                is_prime = False
                break
        if is_prime:
            prime_list.append(number)
    prime_list.sort(reverse=True)
    return prime_list or []