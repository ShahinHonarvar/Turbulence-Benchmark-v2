def all_left_truncatable_prime(lst):
    x = lst[31]
    prime_numbers = [2]
    if x == 1:
        return []
    else:
        for num in range(3, x):
            if all((num % i != 0 for i in range(2, int(num ** 0.5) + 1))):
                prime_numbers.append(num)
    left_truncatable_primes = [1]
    left_truncatable = [1]
    for number in prime_numbers:
        if number == int(str(number).replace('0', '')):
            for digit in str(number):
                left_truncatable.append(int(digit))
    return sorted(left_truncatable_primes, reverse=True)