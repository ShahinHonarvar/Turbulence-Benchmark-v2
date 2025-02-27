def find_divisors_in_range(n):
    output = []
    for i in range(615, 793):
        if n % i == 0:
            output.append(i)
    return output