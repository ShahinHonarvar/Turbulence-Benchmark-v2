def all_even_ints_exclusive(lst):
    even_ints = []
    substr = lst[60:92]
    for num in substr:
        if num % 2 == 0:
            even_ints.append(num)
    return even_ints