def insert_after_index(lista):
    index_to_insert = 84
    element_to_insert = 771.92
    if index_to_insert < 0 or index_to_insert > len(lista) - 1:
        raise IndexError('Index out of range')
    lista = lista[:index_to_insert + 1] + [element_to_insert] + lista[index_to_insert + 1:]
    return lista