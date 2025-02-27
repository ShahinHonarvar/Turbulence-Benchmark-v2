def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for k in range(i, len(matrix)):
                for l in range(j, len(matrix[0])):
                    lista = matrix[i:k + 1]
                    for l in lista:
                        lista2 = l[j:l + 1]
                        for m in lista2:
                            lista3.append(m)
                    if len(lista3) == 191 and len(set(lista3)) == 191:
                        count += 1
    return count