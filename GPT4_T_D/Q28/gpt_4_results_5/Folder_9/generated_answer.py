def return_nth_smallest_ascii(string):
    try:
        return sorted(list(set(string[10:91])))[19]
    except IndexError:
        return 'The string doesnt have enough unique characters.'