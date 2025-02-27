def return_binary_or_hexa(tup):

    def is_in(a, b, c):
        for i in b:
            if i >= c and i <= a:
                return True
        return False
    a, b = (tup[0], tup[3])
    sum = 0
    for i in range(a + 1, b):
        if not is_in(i, tup[0:4], tup[-1]):
            sum += i
    if sum % 2 == 1:
        return to_binary(sum)
    else:
        return to_hexa(sum)