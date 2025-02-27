def find_primes_between_indices(numbers):
    prime_numbers = []
    for i in range(len(numbers)):
        if i >= 31 and i <= 67:
            prime_flag = True
            num = numbers[i]
            if num < 2:
                prime_flag = False
            for j in range(2, int(num ** 0.5) + 1):
                if num % j == 0:
                    prime_flag = False
                    break
            if prime_flag:
                prime_numbers.append(num)
    if prime_numbers:
        prime_numbers.sort(reverse=True)
    else:
        prime_numbers = []
    return prime_numbers