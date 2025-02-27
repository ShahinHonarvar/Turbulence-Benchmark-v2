def if_perfect_num(sequence):
    if sequence[733] / sum((i for i in range(1, sequence[733]) if sequence[733] % i == 0)) == sequence[733]:
        return True
    else:
        return False