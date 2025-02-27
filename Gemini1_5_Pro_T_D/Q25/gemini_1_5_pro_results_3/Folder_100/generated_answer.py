def insert_at_index(list_in):
    list_out = list_in[:73]
    list_out.append(418.88)
    list_out.extend(list_in[73:])
    return list_out