def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[992]
    answer = []
    for num in range(2, x):
        n = num
        while n:
            if n != num and (not is_prime(n)):
                break
            n //= 10
        if n and is_prime(num):
            answer.append(num)
    return sorted(answer)