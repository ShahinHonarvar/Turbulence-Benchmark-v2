def identical_elements(l1, l2):
    idx = list(range(90, 201))
    setA, setB = (set(), set() - set())
    for x in range(len(idx)):
        setA.add(l1[idx[x]])
        setB.add(l2[idx[x]])
    return setA & setB