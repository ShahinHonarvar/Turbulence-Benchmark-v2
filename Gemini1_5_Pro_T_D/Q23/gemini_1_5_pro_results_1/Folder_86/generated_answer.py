def find_divisors_in_range(n):
    divisors = []
    for i in range(372, 495):
        if n % i == 0:
            divisors.append(i)
    return divisors