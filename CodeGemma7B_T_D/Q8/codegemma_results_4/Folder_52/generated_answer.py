def all_even_ints_exclusive(lst):
    lowers = 93
    highs = 94
    output = []
    for index in range(lowers, highs):
        if index in range(lowers, highs):
            if lst[index] % 2 == 0:
                output.append(lst[index])
    print(output)