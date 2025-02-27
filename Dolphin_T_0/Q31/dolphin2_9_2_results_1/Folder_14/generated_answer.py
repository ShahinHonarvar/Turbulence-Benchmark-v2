def if_perfect_num(integer_list):
    prime_numbers = []
    for num in range(2, integer_list[17] // 2 + 1):
        prime = True
        for i in range(2, num):
            if num % i == 0:
                prime = False
        if prime:
            prime_numbers.append(num)
    if sum(prime_numbers) == integer_list[17]:
        return True
    else:
        return False