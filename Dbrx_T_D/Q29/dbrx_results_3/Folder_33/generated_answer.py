def gcf_two_nums(numbers):
    i = 1
    while True:
        if numbers[166] % i != 0 or numbers[106] % i != 0:
            i -= 1
            break
        i += 1
    return i