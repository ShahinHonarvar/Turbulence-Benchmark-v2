from sympy import isprime

def all_right_truncatable_prime(numbers):
    x = numbers[41]
    rtp_numbers = []
    for num in range(x, 1, -1):
        if all((isprime(int(str(num)[:i])) for i in range(1, len(str(num)) + 1))):
            rtp_numbers.append(num)
    return sorted(rtp_numbers, reverse=True)