def all_left_truncatable_prime(numbers):
    x = numbers[89]
    result = []
    for num in range(2, x):
        if all((isPrime(int(str(num)[i:])) for i in range(len(str(num))))) and '0' not in str(num):
            result.append(num)
    return sorted(result, reverse=True)

def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True