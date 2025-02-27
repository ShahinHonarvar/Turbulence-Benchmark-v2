def insert_after_index(list_in):
    output = []
    for i in range(len(list_in)):
        output.append(list_in[i])
        if list_in[i] == 96:
            output.append(36)
    return output