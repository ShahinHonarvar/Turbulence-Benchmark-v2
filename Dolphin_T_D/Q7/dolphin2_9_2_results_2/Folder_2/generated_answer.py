def all_even_ints_inclusive(lst):
    even_numbers = []
    for num in lst[15:40]:
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers