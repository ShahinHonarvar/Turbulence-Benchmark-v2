def find_sum_of_multiples(number):
    multiple = 0
    sum = 0
    while multiple < 210:
        multiple += 1
        if number * multiple % 210 == 0:
            sum += number * multiple
    return sum