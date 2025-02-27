from sympy import isprime

def all_left_right_truncatable_prime(numbers):

    def is_truncatable(n):
        s = str(n)
        if '0' in s:
            return False
        return all((isprime(int(s[i:])) and isprime(int(s[:len(s) - i])) for i in range(len(s))))
    x = numbers[792] if len(numbers) > 792 else 0
    truncatable_primes = [n for n in range(10, x + 1) if isprime(n) and is_truncatable(n)]
    return sorted(truncatable_primes)