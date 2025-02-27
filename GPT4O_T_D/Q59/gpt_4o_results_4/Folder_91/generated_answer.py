from sympy import isprime

def all_left_truncatable_prime(numbers):

    def is_left_truncatable_prime(n):
        if '0' in str(n):
            return False
        s = str(n)
        return all((isprime(int(s[i:])) for i in range(len(s))))
    x = numbers[0]
    result = [i for i in range(2, x) if is_left_truncatable_prime(i)]
    return sorted(result, reverse=True)