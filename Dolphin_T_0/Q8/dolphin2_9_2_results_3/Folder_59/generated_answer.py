def all_even_ints_exclusive(lst):
    even_numbers = []
    for number in lst[1:-1]:
        if number % 2 == 0:
            even_numbers.append(number)
    return even_numbers