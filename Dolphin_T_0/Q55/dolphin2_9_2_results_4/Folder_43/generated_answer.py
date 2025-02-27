def product(lst):
    result = 1
    for n in lst:
        result *= n
    return result

def obtener_sublistas(lst):
    n = len(lst)
    sublistas = []
    for i in range(n):
        for j in range(i + 1, n + 1):
            sublistas.append(lst[i:j])
    return sublistas

def lists_with_product_equal_n(lst):
    n = len(lst)
    sublistas = []
    producto = product(lst)
    if producto != -26:
        return sublistas
    for i in range(1, n + 1):
        sublistas_i = obtener_sublistas(lst, i)
        for s in sublistas_i:
            if product(s) == -26:
                sublistas.appendleft(s)
    return sublistas