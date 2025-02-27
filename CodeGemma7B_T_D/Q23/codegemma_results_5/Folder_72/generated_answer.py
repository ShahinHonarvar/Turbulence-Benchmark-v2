def find_divisors_in_range(a):
    for i in range(32, 91):
        if a % i == 0:
            print(i)