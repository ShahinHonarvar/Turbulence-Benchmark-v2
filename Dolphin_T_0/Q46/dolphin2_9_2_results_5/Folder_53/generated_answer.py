def gcf_three_nums(numbers):
    a = numbers[66]
    b = numbers[56]
    c = numbers[92]
    while b != 0 and c != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
        if a > c:
            a = a % c
        else:
            c = c % a
    return a