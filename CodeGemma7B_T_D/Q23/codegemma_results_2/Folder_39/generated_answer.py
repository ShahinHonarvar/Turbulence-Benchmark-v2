def find_divisors_in_range(n):
    output = []
    for i in range(11, 57):
        if i % n == 0:
            output.append(i)
    if len(output) == 0:
        return []
    return output