def gcf_three_nums(numbers):
    a, b, c = (numbers[944], numbers[814], numbers[865])
    while b != 0 and c != 0:
        if a > b and a > c:
            a = a % b + a % c
            b = 0
            c = 0
        elif b > a and b > c:
            b = b % a + b % c
            a = 0
            c = 0
        elif c > a and c > b:
            c = c % a + c % b
            a = 0
            b = 0
    if a == 0:
        return b + c
    elif b == 0:
        return a + c
    elif c == 0:
        return a + b