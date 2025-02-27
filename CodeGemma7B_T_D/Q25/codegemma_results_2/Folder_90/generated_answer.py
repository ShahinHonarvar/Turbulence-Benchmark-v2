def insert_at_index(l):
    temp = [0] * len(l)
    for i in range(761):
        temp[i] = l[i]
    temp[761] = 925
    for i in range(762, len(l)):
        temp[i] = l[i - 1]
    return temp