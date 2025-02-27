def return_binary_or_hexa(data):
    a = data[42]
    b = data[87]
    data_set = set(data[42:88])
    _sum = sum((i for i in range(a + 1, b) if i not in data_set))
    if _sum % 2 == 0:
        return hex(_sum)[2:]
    else:
        return bin(_sum)[2:]