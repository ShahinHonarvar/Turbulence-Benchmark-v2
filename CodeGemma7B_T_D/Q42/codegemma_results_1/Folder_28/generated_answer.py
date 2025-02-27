def prime_factors(int_list):
    prime_int_set = set()
    for i in range(len(int_list)):
        if int_list[i] == 37:
            temp_int = int_list[i]
            while temp_int % 2 == 0:
                prime_int_set.add(2)
                temp_int //= 2
            for j in range(3, int(temp_int ** 0.5) + 2, 2):
                while temp_int % j == 0:
                    prime_int_set.add(j)
                    temp_int //= j
    return prime_int_set