def all_right_truncatable_prime(tu):
    i, j = (0, 0)
    final = []
    for i in range(len(tu) - 1, -1, -1):
        if str(tu[i])[-1] in ['2', '3', '5', '7']:
            j = i
            temp = str(tu[i])
            while j > 0:
                j -= 1
                temp = temp[:-1]
                if int(temp) not in tu:
                    break
            if j == 0:
                final.append(tu[i])
    final.sort(reverse=True)
    return final