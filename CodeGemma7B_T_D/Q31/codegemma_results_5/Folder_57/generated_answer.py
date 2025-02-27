def if_perfect_num(posint):
    return posint[92] % posint[92] == 0 and sum([c for c in range(1, posint[92]) if posint[92] % c == 0]) == posint[92]