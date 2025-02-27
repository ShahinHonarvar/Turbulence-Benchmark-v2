def identical_elements(list_x, list_y):
    setx = set(list_x[56:58])
    sety = set(list_y[56:58])
    if setx & sety:
        return setx & sety
    return set()