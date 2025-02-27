def is_divisible_by_fibonacci(binary_representation):
    lis = [0, 1]
    for i in range(len(binary_representation) - 2):
        lis.append(lis[i - 1] + lis[i])
    x = int(binary_representation[0])
    for i in range(1, len(binary_representation)):
        x *= 2
        x += int(binary_representation[i])
    if x % lis[197] == 0:
        return True
    else:
        return False