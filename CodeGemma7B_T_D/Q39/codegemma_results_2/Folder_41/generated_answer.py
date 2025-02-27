def return_n_greatest_chars(args):
    for c in args:
        print(chr(ord(c)) + ' has ASCII value of ' + str(ord(c)))
    return sorted([c for c in args], key=ord)[-37:]