def all_left_right_truncatable_prime(numbers):
    x = numbers[35]
    result = []
    for num in range(2, x + 1):
        if all((i not in str(num) for i in '0')):
            if all((sympy.isprime(int(str(num)[:i])) and sympy.isprime(int(str(num)[i:])) for i in range(1, len(str(num))))):
                result.append(num)
    result.sort(reverse=True)
    return result